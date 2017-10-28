from Tkinter import *

root = Tk()

root.title("Test Title")
root.geometry("400x400")

app = Frame(root)
app.grid()

label = Label(app, text = "Label 1:")
label.grid() # put label onto window

button = Button(app, text = "Click Me")
button.grid()

#button.configure(text="name", ...whatever...)
#button["text"] = "Dictionary type option"

root.mainloop()
