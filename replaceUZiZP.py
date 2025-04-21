import os
import copy
import xml.etree.ElementTree as ET

class replace:

    def __init__(self, path: str, progress_callback=None):
        self.folder_path = path
        self.progress_callback = progress_callback
        self.input_files = [
            os.path.join(self.folder_path, f)
            for f in os.listdir(self.folder_path) if f.endswith('.xml')
        ]

    def get_snils(self, zl_elem):
        for elem in zl_elem.iter():
            if elem.tag.endswith('СНИЛС'):
                return elem.text.strip()
        return None

    def get_uzizp_blocks(self, zl_elem):
        return [el for el in zl_elem.iter() if el.tag.endswith('УЗиЗП')]

    def get_szpgos(self, zl_elem):
        for el in zl_elem.iter():
            if el.tag.endswith('СЗПГос'):
                return el
        return None

    def get_vid(self, uzizp_element):
        for elem in uzizp_element.iter():
            if elem.tag.endswith('Вид'):
                return elem.text.strip()
        return None

    def strip_ns(self, root_element):
        for el in root_element.iter():
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]
            el.attrib = {
                (k.split('}', 1)[1] if '}' in k else k): v
                for k, v in el.attrib.items()
            }

    def start(self):
        # --- Сбор данных ---
        snils_to_main = {}  # СНИЛС -> (zl_element, tree, file)
        all_zl_entries = []  # [(snils, zl, tree, file)]

        for file in self.input_files:
            tree = ET.parse(file)
            root = tree.getroot()
            self.strip_ns(root)

            for zl in root.iter():
                if not zl.tag.endswith('ЗЛ'):
                    continue
                snils = self.get_snils(zl)
                if not snils:
                    continue

                all_zl_entries.append((snils, zl, tree, file))

                for uz in self.get_uzizp_blocks(zl):
                    if self.get_vid(uz) == '1' and snils not in snils_to_main:
                        snils_to_main[snils] = (zl, tree, file)
                        break

        # --- Обработка и прогресс ---
        total = len(snils_to_main)
        done = 0
        last_percent = -1

        for snils, (main_zl, main_tree, main_file) in snils_to_main.items():
            szpgos_main = self.get_szpgos(main_zl)
            if szpgos_main is None:
                continue

            modified_secondary_files = set()

            for s, zl, tree, file in all_zl_entries:
                if s != snils or zl is main_zl:
                    continue

                szpgos_other = self.get_szpgos(zl)
                if szpgos_other is None:
                    continue

                uzizp_list = self.get_uzizp_blocks(zl)
                for uz in uzizp_list:
                    szpgos_main.append(copy.deepcopy(uz))
                    szpgos_other.remove(uz)
                    modified_secondary_files.add(file)

            # Сохраняем основной файл
            main_tree.write(main_file, encoding='utf-8', xml_declaration=True)

            # Сохраняем вторичные файлы
            for f in modified_secondary_files:
                for _, _, tree_candidate, tree_file in all_zl_entries:
                    if tree_file == f:
                        tree_candidate.write(f, encoding='utf-8', xml_declaration=True)
                        break

            # Прогресс
            done += 1
            percent = int((done / total) * 100)
            if percent != last_percent:
                if self.progress_callback:
                    self.progress_callback(f"{percent}%")
                else:
                    print(f"{percent}%")
                last_percent = percent
