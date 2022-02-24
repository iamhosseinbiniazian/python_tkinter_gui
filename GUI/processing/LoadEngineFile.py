import io
from tkinter import *
from tkinter import  ttk
from tkinter import filedialog
import collections
class engineFile:
    def __init__(self,path='./option.txt'):
        self.path=path
        self.data=collections.OrderedDict()
    def loadFile(self):
        self.data.clear()
        filePath = filedialog.askopenfilename(filetypes=(("txt File", "*.txt")
                                   , ("All files", "*.*")))
        with io.open(file=filePath,mode='r') as file:
            for line in file:
                words=line.strip().rstrip()
                if words!='':
                    print(words)
                    words=words.split(' ')
                    self.data[(words[0],words[1])]=int(words[2])
        self.path=filePath

    def saveFile(self):
        filePath = filedialog.asksaveasfilename(filetypes=(("txt File", "*.txt")
                                   , ("All files", "*.*")))
        with io.open(file=filePath,mode='w') as file:
            for key, value in self.data.items():
                file.write(key[0]+' '+key[1]+' '+str(value)+'\n')




