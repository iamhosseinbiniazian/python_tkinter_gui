from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
class ProcessBar:
    def __init__(self,root):
        self.root = root
        self.Pbar =ttk.Progressbar(root)
        self.Pbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
        self.Pbar.pack(fill=BOTH, expand=True)