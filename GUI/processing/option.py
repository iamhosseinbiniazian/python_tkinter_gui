from GUI.processing.LoadEngineFile import engineFile
from GUI.processing.configure import Configure
from GUI.ui.TreeView import Multicolumn_Listbox
from GUI.ui.MenuBar import Menubar
from GUI.ui.mesagebox import MessageBox
from GUI.ui.Pbar import ProcessBar
from tkinter import *
class Option(object):
    def __init__(self,self2):
        self.root=self2
        self.engineFile= engineFile()
        self.configure=Configure()
        self.treeView=Multicolumn_Listbox(self2.frameTreeView, ["index","Folder", "KeyWord", "Number"],
                                    cell_anchor="center",heading_anchor=W,adjust_heading_to_content=True)
        self.treeView.interior.pack(fill=BOTH, expand=True)
        self.menuBar=Menubar(self2.root,self)
        self.messageBox=MessageBox(self2.labelFrameRightUpRight)
        self.Pbar=ProcessBar(self2.labelFrameRightDownRight)
    def loadEngineFile(self):
        self.engineFile.loadFile()
        self.updateTreeView()
    def saveEngineFile(self):
        self.engineFile.saveFile()
    def updateTreeView(self):
        self.treeView.clear()
        for key,value in self.engineFile.data.items():
            self.treeView.insert_row([self.treeView.number_of_rows+1,key[0],key[1],value],index=self.treeView.number_of_rows+1)


