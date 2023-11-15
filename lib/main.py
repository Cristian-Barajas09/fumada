import tkinter as tk
from lib.translate_content import TranslateContent
class App:
    def __init__(self,intance: tk.Tk,file: str):
        self.instance_app = intance()
        self.translate_content = TranslateContent(file)

    def run(self):
        self.translate_content.translate(window=self.instance_app)
        self.instance_app.mainloop()

    def title(self):
        self.instance_app.title('PyML')