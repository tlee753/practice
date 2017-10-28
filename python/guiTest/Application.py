# use a class with tinker

from Tkinter import *

class Application(Frame):
    """ Example Docstring """

    def __init__(self, master):
        """ another doc string """
        Frame.__init__(self, master)
        self.button_clicks = 0
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ create a small widget """
        self.button = Button(self, text="Click Me")
        self.button.grid()
        self.button["command"] = self.update_count

    def update_count(self):
        """ increase count and display total """
        self.button_clicks += 1
        self.button["text"] = "Total Clicks: "  + str(self.button_clicks)

root = Tk()

root.title("buttons")
root.geometry("400x400")

app = Application(root)

root.mainloop()