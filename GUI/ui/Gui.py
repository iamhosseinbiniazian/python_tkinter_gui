from tkinter import *
from tkinter import ttk
from GUI.ui.customButton import CustomButton
from GUI.processing.controler import Controler
from GUI.ui.resizingcanvas import ResizingCanvas
class Gui:
    def __init__(self,root):
        self.root=root
        self.root.option_add('*tearOff', False)
        # root.attributes('-zoomed', True)
        self.root.title("NDC")
        ###########################shortcut bar################################
        self.shortcut_bar = Frame(self.root, height=25, background='light sea green')
        self.shortcut_bar.pack(expand=NO, fill=X)
        ##############################################################
        self.mainPanedWindow = ttk.Panedwindow(root, orient=HORIZONTAL)
        self.mainPanedWindow.pack(fill=BOTH, expand=True)
        self.frameLeft = ttk.Frame(self.mainPanedWindow, width=120, height=300, relief=SUNKEN)
        self.frameRight = ttk.Frame(self.mainPanedWindow, width=400, height=400, relief=SUNKEN)
        self.mainPanedWindow.add(self.frameLeft, weight=1)
        self.mainPanedWindow.add(self.frameRight, weight=10)
        #########################################################################
        self.NDCPanedWindow = ttk.Panedwindow(self.frameLeft, orient=HORIZONTAL)
        self.NDCPanedWindow.pack(fill=BOTH, expand=True)
        self.frameTreeView = ttk.Frame(self.NDCPanedWindow, width=100, height=400, relief=SUNKEN)
        self.frameNDC = ttk.Frame(self.NDCPanedWindow, width=300, height=self.root.winfo_screenheight(), relief=SUNKEN)
        self.NDCPanedWindow.add(self.frameTreeView, weight=1)
        self.NDCPanedWindow.add(self.frameNDC, weight=0)
        ##############################################################
        #U=Up
        #B=Between
        #D=Down
        #L=Left
        #R=Right
        self.NDCCPanedWindow = ttk.Panedwindow(self.frameNDC, orient=HORIZONTAL)
        self.NDCCPanedWindow.pack(fill=BOTH, expand=True)
        canvas_width = self.NDCCPanedWindow.winfo_screenmmwidth()
        print(canvas_width)
        canvas_height =self.NDCCPanedWindow.winfo_screenheight()-50
        print(canvas_height)

        python_green = "#476042"
        # canvasU = Canvas(self.NDCCPanedWindow,width=canvas_width,height=canvas_height)
        canvasU = ResizingCanvas(self.NDCCPanedWindow , width=canvas_width, height=canvas_height, bg="gray", highlightthickness=0)
        canvasU.pack(fill=BOTH, expand=YES)
        canvas_height=canvas_height/2
        newh=canvas_height
        canvas_height=canvas_height-20
        points = [0, 0,
                  canvas_width, 0,
                  canvas_width, canvas_height,
                  ######################
                  canvas_width-(canvas_width/3), canvas_height,
                  ###############################
                  canvas_width - ((canvas_width / 3)+((canvas_width )/18)), canvas_height-canvas_height/8,
                  (canvas_width / 3) + ((canvas_width ) / 18), canvas_height -canvas_height/8,
                  (canvas_width / 3), canvas_height,
                  0, canvas_height]
                  # 110, 90,
                  # 100, 60,
                  # 90, 90,
                  # 60, 100,
                  # 90, 110]
        canvas_height=newh

        points1 = [
            0,canvas_height,
            (canvas_width / 3),canvas_height,
            (canvas_width / 3)+((canvas_width ) / 18),canvas_height/8+canvas_height,
            canvas_width-((canvas_width / 3)+((canvas_width ) / 18)),canvas_height/8+canvas_height,
            canvas_width - (canvas_width/3), canvas_height,
            canvas_width,canvas_height,
            canvas_width, canvas_height*2,
            0, canvas_height*2,
        ]
        # canvas_height = canvas_height - 20
        points21 = [
            (canvas_width / 3), canvas_height,
            (canvas_width / 3) + ((canvas_width) / 18), canvas_height / 8 + canvas_height,
            canvas_width - ((canvas_width / 3) + ((canvas_width) / 18)), canvas_height / 8 + canvas_height,
            canvas_width - (canvas_width / 3), canvas_height,


        ]
        canvas_height = canvas_height - 20
        points22=[
            canvas_width - (canvas_width / 3), canvas_height,
            ###############################
            canvas_width - ((canvas_width / 3) + ((canvas_width) / 18)), canvas_height - canvas_height / 8,
            (canvas_width / 3) + ((canvas_width) / 18), canvas_height - canvas_height / 8,
            (canvas_width / 3), canvas_height,

        ]
        points2=points21+points22
        rectanglepoint=[
            (canvas_width / 3) + ((canvas_width) / 18), canvas_height - canvas_height / 8,
            points2[4] ,points2[5],
        ]
        canvasU.create_polygon(points, outline=python_green,
                         fill='blue', width=3)

        canvasU.create_polygon(points1, outline=python_green,
                          fill='red', width=3)
        canvasU.create_polygon(points2, outline=python_green,
                          fill='yellow', width=3,tags='obj2Tag')
        # c=CustomButton(canvasU,rectanglepoint)


        # canvasD = Canvas(self.frameNDC)
        # canvasD.pack(side="bottom")
        # canvasU.config(width=self.frameNDC.winfo_width(),height=self.frameNDC.winfo_height())
        # canvasD.config(width=300,height=200)
        # x=canvasU.cget("width")
        # y=canvasU.winfo_height()/2
        # print(x,' ',y)
        #
        # poly = canvasU.create_polygon(0, 0, 0,x,x,y,0,y, fill='blue')
        # poly = canvasD.create_polygon(0, 0, 200, 0, 200, 200, 0, 200, fill='red')

        # root.mainloop()

        ###############################################################
        self.rightPanedWindow = ttk.Panedwindow(self.frameRight, orient=VERTICAL)
        self.rightPanedWindow.pack(fill=BOTH, expand=True)
        self.frameRightUp = ttk.Frame(self.rightPanedWindow, width=100, height=400, relief=SUNKEN)
        self.frameRightDown = ttk.Frame(self.rightPanedWindow, width=400, height=100, relief=SUNKEN)
        self.rightPanedWindow.add(self.frameRightUp, weight=4)
        self.rightPanedWindow.add(self.frameRightDown, weight=1)
        ##################################################################
        self.rightUpPanedWindow=ttk.Panedwindow(self.frameRightUp, orient=HORIZONTAL)
        self.frameRightUpLeftStyle = ttk.Style()
        self.frameRightUpLeftStyle.configure('My.TFrame', background='white')
        self.rightUpPanedWindow.pack(fill=BOTH, expand=True)
        self.frameRightUpLeft = ttk.Frame(self.rightUpPanedWindow,style='My.TFrame', width=100, height=300, relief=SUNKEN)
        self.frameRightUpRight = ttk.Frame(self.rightUpPanedWindow, width=400, height=400, relief=SUNKEN)
        self.rightUpPanedWindow.add(self.frameRightUpLeft,weight=1)
        self.rightUpPanedWindow.add(self.frameRightUpRight,weight=4)


        ####################################################################
        self.rightUpRightPanedWindow = ttk.Panedwindow(self.frameRightUpRight, orient=VERTICAL)
        self.rightUpRightPanedWindow.pack(fill=BOTH, expand=True)
        self.frameMbox = ttk.Frame(self.rightUpRightPanedWindow, width=100, height=400, relief=SUNKEN)
        self.framePbar = ttk.Frame(self.rightUpRightPanedWindow, width=400, height=100, relief=SUNKEN)
        self.rightUpRightPanedWindow.add(self.frameMbox, weight=4)
        self.rightUpRightPanedWindow.add(self.framePbar, weight=1)
        self.labelFrameRightUpRight=LabelFrame(self.frameMbox,text="Logs",relief = RIDGE)
        self.labelFrameRightUpRight.pack(fill=BOTH,expand=True)
        self.labelFrameRightUpRight.config()
        self.labelFrameRightDownRight = LabelFrame(self.framePbar, text="Download Process", relief=RIDGE)
        self.labelFrameRightDownRight.pack(fill=BOTH, expand=True)
        self.labelFrameRightDownRight.config()
        ############################################################
        self.controler=Controler(self)

