import os
import xml.etree.ElementTree as ET
import copy

class replace:

    def __init__(self):
        self.folder_path = 'D:/- dev/xmc1C/files/2025/test'
        self.input_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith('.xml')]

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

    def start(self):
        # --- Сбор данных ---
        snils_to_main = {}  # СНИЛС -> (zl_element, tree, file)
        all_zl_entries = []

        for file in self.input_files:
            tree = ET.parse(file)
            root = tree.getroot()

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

        # --- Обработка с прогрессом ---
        total = len(snils_to_main)
        done = 0
        last_percent = -1

        for snils, (main_zl, main_tree, main_file) in snils_to_main.items():
            szpgos = self.get_szpgos(main_zl)
            if szpgos is None:
                continue

            for s, zl, _, _ in all_zl_entries:
                if s != snils or zl is main_zl:
                    continue
                for uz in self.get_uzizp_blocks(zl):
                    szpgos.append(copy.deepcopy(uz))

            # Сохраняем изменения
            main_tree.write(main_file, encoding='utf-8', xml_declaration=True)

            # Обновляем процент выполнения
            done += 1
            percent = int((done / total) * 100)
            if percent != last_percent:
                print(f'{percent}%')
                last_percent = percent