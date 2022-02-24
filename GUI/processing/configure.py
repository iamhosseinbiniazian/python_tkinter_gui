import collections
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import io
import json
class Configure:
    def __init__(self,path="./config"):
        '''
        :param path:
        '''
        self.path=path
        self.option = collections.OrderedDict()
        #self.option['engine'] = ["Google","Flickr","Bing"]
        self.option['engine'] = []
        self.option['safe search']=BooleanVar(False)
        self.option['exclude'] = ["*/.svn", "*/.bzr"],
        self.option['dry_run'] = None
        self.option['prefer'] = []
        self.option['defaults'] = BooleanVar(False)
        self.option['exact'] = BooleanVar(False)
        self.option['min_size'] = 25
        self.option['noninteractive'] = None
        self.option['deletedup'] = BooleanVar(False)
        self.option['dir'] ='/home/apasai'
        self.googleEngine = BooleanVar()
        self.bingEngine = BooleanVar()
        self.flickrEngine = BooleanVar()
    def GoogleEngineChoose(self):
        if self.googleEngine.get():
            if 'Google' not in self.option['engine']:
                self.option['engine'].append('Google')
        else:
            if 'Google' in self.option['engine']:
                b = self.option['engine'].index('Google')
                del self.option['engine'][b]
        print("*******************************")
        print(self.option['engine'])
        print("*******************************")
    def BingEngineChoose(self):
        if self.bingEngine.get():
            if 'Bing' not in self.option['engine']:
                self.option['engine'].append('Bing')
        else:
            if 'Bing'  in self.option['engine']:
                b = self.option['engine'].index('Bing')
                del self.option['engine'][b]
        print("*******************************")
        print(self.option['engine'])
        print("*******************************")
    def FlickrEngineChoose(self):
        if self.flickrEngine.get():
            if 'Flickr' not in self.option['engine']:
                self.option['engine'].append('Flickr')
        else:
            if 'Flickr' in self.option['engine']:
                b = self.option['engine'].index('Flickr')
                del self.option['engine'][b]
        print("*******************************")
        print(self.option['engine'])
        print("*******************************")
    def loadConfigure(self):
        filePath=filedialog.askopenfilename(filetypes = (("Jason File", "*.json")
                                                         ,("All files", "*.*")))
        if filePath:
            try:
                print('read:',filePath)
                with io.open(filePath,mode='r') as file:
                    data = json.load(file)
                    for key , value in data.items():
                            if value in [0,1]:
                                self.changeOption(bool(value), optionname=key)
                            elif value == 'None':
                                self.changeOption(None, optionname=key)
                            else:
                                self.changeOption(value, optionname=key)
                self.path=filePath
                print(self.option)

            except:
                messagebox.showerror("Open Source File", "Failed to read file \n'%s'" % filePath)
    def changeOption(self,value,optionname='engine'):
        self.option[optionname]=value




