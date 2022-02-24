import tkinter as tk
class CustomButton(tk.Canvas):
    def __init__(self, parent, point, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1,
                           relief="raised", highlightthickness=0)
        self.command = command

        padding = 4
        id = parent.create_rectangle(point, outline='green',
                          fill='gray', width=3)
        (x0, y0, x1, y1) = parent.bbox("all")
        button = tk.Button(None, text='Click Me')
        parent.create_window(point[2],point[3],window=button)
        width = (x1 - x0) + padding
        height = (y1 - y0) + padding
        parent.configure(width=point[0], height=point[1])
        parent.tag_bind("obj2Tag", "<ButtonPress-1>",self._on_press)
        # parent.bind("<ButtonPress-1>", self._on_press)
        # parent.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")
        print("Hi")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()