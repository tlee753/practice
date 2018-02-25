from tkinter import *
import tkinter.messagebox


class Main:
    def __init__(self):
        self.root = Tk()

        # ***** menubar *****
        self.mainMenu = Menu(self.root)
        self.root.config(menu=self.mainMenu)

        self.fileMenu = Menu(self.mainMenu)
        self.mainMenu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Open Image...", command=self.openImage)
        self.fileMenu.add_command(label="Close Image...", command=self.closeImage)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Quit", command=self.quit)

        self.editMenu = Menu(self.mainMenu)
        self.mainMenu.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_command(label="Undo", command=self.undo)

        # ***** frame *****
        self.frame = Frame(self.root)
        self.frame.pack()

        self.quitButton = Button(self.frame, text="Quit", command=self.frame.quit)
        self.quitButton.pack()

        # ***** canvas *****
        self.canvas = Canvas(self.root, width=200, height=100)
        self.canvas.pack()
        blackline = self.canvas.create_line(0, 0, 200, 50)
        redline = self.canvas.create_line(0, 100, 200, 50, fill="red")

        # ***** statusbar *****
        self.status = Label(self.root, text="At the dawn of time...", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

        # ***** messagebox *****
        tkinter.messagebox.showinfo("Messagebox Title", "Fun little blurbly text")
        answer = tkinter.messagebox.askquestion("Question 1", "Will you marry me?")
        if answer == "yes":
            print("Halelijah")
        else:
            print("I was kidding jeez")


    def openImage(self):
        print("opening image")

    def closeImage(self):
        print("Closing iamge")

    def quit(self):
        self.frame.quit()

    def undo(self):
        print("undoing your shit")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Main().run()
