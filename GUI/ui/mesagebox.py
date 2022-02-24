from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
class MessageBox:
    def __init__(self,root):
        self.root=root
        self.MBox=Text(root,wrap='word')
        self.MBox.pack(fill=BOTH,expand=True)
        self.scroll_bar = Scrollbar(self.MBox)
        self.MBox.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.MBox.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)
        self.MBox.config(state=DISABLED)