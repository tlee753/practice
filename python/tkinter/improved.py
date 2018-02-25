from tkinter import *


class Main:
    def __init__(self, root):
        self.frame = Frame(root, width=500, height=500, bg="black")
        self.frame.pack(fill=None, expand=False)

        self.quitButton = Button(self.frame, text="Quit", command=self.frame.quit)
        self.quitButton.pack()

root = Tk()
m = Main(root)
root.mainloop()