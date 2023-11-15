import re
from lib.search import Search
from lib.dict_tags import DictTags

class TranslateContent:
    def __init__(self,file):
        self.search_files = Search(file)

    def translate(self,window):
        result = self.clean_tags()
        content,text = self.translate_tags(result)

        for tag in content:
            try:
                print(text)
                instance = DictTags[tag[0]](master=window,text=text[0])
                instance.pack()
            except KeyError as error:
                pass

    def clean_tags(self):
        clean = []
        content = self.search_files.content_files()
        for content_file in content.values():
            for values in content_file:
                clean.append(values.strip('\n'))

        return clean

    def translate_tags(self,contents: list):
        coincidences = []
        clean = contents.copy()
        for content in contents:
            result = re.findall(r'(<.*?>)',content)
            if result:
                coincidences.append(result)
                clean.remove(content)
        return coincidences,clean
