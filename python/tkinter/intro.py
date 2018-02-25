from tkinter import *

# initialize tk class
root = Tk()


root.minsize(width=500, height=500)

def goFuckYourSelf(event):
    print("Go fuck yourself")

def rightClick(event):
    print("Go right yourself")


topFrame = Frame(root, width=500, height=500)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red", bg="black")
button1.bind("<Button-1>", goFuckYourSelf)
button1.bind("<Button-2>", rightClick)
button2 = Button(topFrame, text="Button 2", fg="blue")
# button3 = Button(topFrame, text="Button 3", fg="green")
# button4 = Button(bottomFrame, text="Button 4", fg="yellow")
#
button1.pack(side=LEFT)
button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)

entry1 = Entry(bottomFrame)
checkbox1 = Checkbutton(bottomFrame, text="whyNot")

entry1.grid(row=0, column=0)
checkbox1.grid(row=1, columnspan=2)

# run mainloop
root.mainloop()
