from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
class Menubar:
    def __init__(self,root,option):
        self.root = root
        self.new_file_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons/new_file.gif')
        self.open_file_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//open_file.gif')
        self.save_file_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//save.png')
        self.save_as_file_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//save_as.png')
        self.cut_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//cut.gif')
        self.copy_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//copy.gif')
        self.paste_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//paste.gif')
        self.undo_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//undo.gif')
        self.redo_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//redo.gif')
        self.google_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//google.png')
        self.bing_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//bing.png')
        self.flickr_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//flicker.png')
        self.engine_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//engine.png')
        self.safe_search_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//safesearch.png')
        self.yes_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//yes.png')
        self.no_icon = PhotoImage(file='D:/My Plan/Project/Source Code/Not Pay/NDCrawler/GUI/ui/icons//no.png')
        ###########################################################
        self.mainMenu,self.fileMenu,self.optionMenu,self.helpMenu=self.createMainMenu()
        self.safeSearchMenu=self.createSafeSearchMenu(option)
        self.engineMenu=self.createEngineMenu(option)
        self.configureMenu=self.createConfigureMenu(option)
        self.loadEngineFileMenu=self.createLoadEngineFileMenu(option)
    def Exit(self):
        self.root.destroy()
    def createMainMenu(self):
        #########################Main Menu#############################
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        file = Menu(menubar)
        option = Menu(menubar)
        help_ = Menu(menubar)
        menubar.add_cascade(menu=file, label='File')
        menubar.add_cascade(menu=option, label='Option')
        menubar.add_cascade(menu=help_, label='Help')
        file.add_command(label='Exit', command=self.Exit)
        file.entryconfig('Exit', accelerator='Alt+F4')
        return (menubar,file,option,help_)
    def createSafeSearchMenu(self,option):
        ####################################################################
        ###########Safe Search Menu#########################################
        safeSearch = Menu(self.optionMenu)
        self.optionMenu.add_cascade(menu=safeSearch, label='Safe Search',image=self.safe_search_icon,compound=LEFT)
        safeSearch.add_radiobutton(label='Yes', variable=option.configure.option['safe search'], value=True,image=self.yes_icon,compound=LEFT)
        safeSearch.add_separator()
        safeSearch.add_radiobutton(label='No', variable=option.configure.option['safe search'], value=False,image=self.no_icon,compound=LEFT)
        return safeSearch
    def createEngineMenu(self,option):
        ##########################Chosse Engine Menu#############################################
        engine = Menu(self.optionMenu)
        self.optionMenu.add_cascade(menu=engine, label='Engine',image=self.engine_icon,compound=LEFT)
        engine.add_checkbutton(label='Google',image=self.google_icon,compound=LEFT,variable=option.configure.googleEngine, command=lambda: option.configure.GoogleEngineChoose())
        engine.add_checkbutton(label='Bing',image=self.bing_icon,compound=LEFT, variable=option.configure.bingEngine, command=lambda :option.configure.BingEngineChoose())
        engine.add_checkbutton(label='Flickr',image=self.flickr_icon,compound=LEFT, variable=option.configure.flickrEngine, command=lambda :option.configure.FlickrEngineChoose())
        return engine
        ######################################################################################
    def createConfigureMenu(self,option):
        ###########################################Configure Menu###############################
        configure = Menu(self.fileMenu)
        self.fileMenu.add_cascade(menu=configure, label="Configure")
        configure.add_command(label='New',compound=LEFT,image=self.new_file_icon,command=lambda :print("New"))
        configure.add_command(label='Load',compound=LEFT,image=self.open_file_icon ,command=option.configure.loadConfigure)
        configure.add_command(label="Save",compound=LEFT,image=self.save_file_icon,command=lambda :print("Save"))
        configure.add_command(label="Save As",compound=LEFT,image=self.save_as_file_icon,command=lambda :print("Save s"))
        return configure
        ########################################################################################
    def createLoadEngineFileMenu(self,option):
        ###########################################Configure Menu###############################
        loadEngineFile = Menu(self.fileMenu)
        self.fileMenu.add_cascade(menu=loadEngineFile, label="Load Engine File")
        loadEngineFile.add_command(label='New',compound=LEFT,image=self.new_file_icon,command=lambda :print("New"))
        loadEngineFile.add_command(label='Load',compound=LEFT,image=self.open_file_icon , command=option.loadEngineFile)
        loadEngineFile.add_command(label="Save",compound=LEFT,image=self.save_file_icon,command=option.saveEngineFile)
        loadEngineFile.add_command(label="Save As",compound=LEFT,image=self.save_as_file_icon,command=lambda :print("Save as"))
        return loadEngineFile
        ########################################################################################
    def loadEngineFile(self):
        filePath = filedialog.askopenfilename(filetypes=(("txt File", "*.txt")#all other extionsion add this line
                                                         , ("All files", "*.*")))
        if filePath:
            try:
                print('read:',filePath)
                loadEngineFile=Loadenginefile(path=filePath)
                loadEngineFile.loadFile()
            except:
                messagebox.showerror("Open Source File", "Failed to read file \n'%s'" % filePath)



