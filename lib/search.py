import os


class Search:
    __FILES = ".pyml"
    __path = __file__
    def __init__(self,path:str):
        self.__path = self.directory(path)


    def content_files(self):
        files_content = {}
        files = os.listdir(self.__path)
        for file in files:

            if os.path.isdir(f'{self.__path}/{file}'):
                break

            if self.isPythonFile(f'{self.__path}/{file}'):
                break

            with open(f'{self.__path}/{file}','r',encoding='utf-8') as f:
                files_content[file] = f.readlines()
                f.close()
        return files_content

    def isPythonFile(self,file):
        files = os.path.splitext(file)
        for file in files:
            if file == '.py':
                return True
            return False


    def directory(self,path):
        return os.path.dirname(path)
