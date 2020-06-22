from tkinter import *



class Info:
    def __init__(self,root):
        self.SETTINGS = Toplevel(root)
        self.SETTINGS.title("Справка")
        width = 1200
        height = 900
        self.usual_text = Text(self.SETTINGS ,width=92, height=50, wrap=WORD, font=("@Microsoft YaHei UI Light", 16),
                                  relief=FLAT,
                                  bg='#F0F0F0', fg='#111111')
        scroll = Scrollbar(self.SETTINGS ,command=self.usual_text.yview)
        self.usual_text.config(yscrollcommand=scroll.set)
        self.usual_text.place(x=30, y=100)

        self.SETTINGS.geometry(
            '{}x{}+{}+{}'.format(width, height, (self.SETTINGS.winfo_screenwidth() - width) // 2,
                                 (self.SETTINGS.winfo_screenheight() - height) // 2))
        self.SETTINGS.minsize(width=900, height=600)
        self.SETTINGS.iconbitmap('icon.ico')
        self.update_texts("Здравствуйте, здесь должен быть текст о пользовании программой, но я ничего не придумал")

    def update_texts(self, usual_text):

        self.usual_text.configure(state='normal')
        self.usual_text.delete(1.0, END)
        self.usual_text.insert(1.0, str(usual_text))
        self.usual_text.configure(state='disabled')
if __name__ == "__main__":
    root = Tk()
    Info(root)
    root.mainloop()