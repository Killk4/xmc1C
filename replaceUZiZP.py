import os
import copy
import xml.etree.ElementTree as ET
from PyQt5.QtCore import QThread, pyqtSignal

class ReplaceThread(QThread):
    progress = pyqtSignal(str)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        from replaceUZiZP import replace

        def progress_callback(percent_text):
            self.progress.emit(percent_text)

        rp = replace(path=self.path, progress_callback=progress_callback)
        rp.start()

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

    def remove_zl_from_tree(self, tree, zl_element):
        for parent in tree.getroot().iter():
            for child in list(parent):
                if child is zl_element:
                    parent.remove(child)
                    return

    def start(self):
        snils_to_main = {}
        all_zl_entries = []

        for file in self.input_files:
            tree = ET.parse(file)
            root = tree.getroot()
            self.strip_ns(root)

            for zl in root.iter('ЗЛ'):
                snils = self.get_snils(zl)
                if not snils:
                    continue

                all_zl_entries.append((snils, zl, tree, file))

                for uz in self.get_uzizp_blocks(zl):
                    if self.get_vid(uz) == '1' and snils not in snils_to_main:
                        snils_to_main[snils] = (zl, tree, file)
                        break

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

                for uz in self.get_uzizp_blocks(zl):
                    uz_copy = copy.deepcopy(uz)

                    # Меняем <Вид> с 3 на 2
                    for elem in uz_copy.iter():
                        if elem.tag == 'Вид' and elem.text == '3':
                            elem.text = '2'

                    szpgos_main.append(uz_copy)

                # Удаление <ЗЛ>
                self.remove_zl_from_tree(tree, zl)
                modified_secondary_files.add(file)

            main_tree.write(main_file, encoding='utf-8', xml_declaration=True)

            for f in modified_secondary_files:
                for _, _, tree_candidate, tree_file in all_zl_entries:
                    if tree_file == f:
                        tree_candidate.write(f, encoding='utf-8', xml_declaration=True)
                        break

            done += 1
            percent = int((done / total) * 100)
            if percent != last_percent:
                if self.progress_callback:
                    self.progress_callback(f"{percent}%")
                else:
                    print(f"{percent}%")
                last_percent = percent
