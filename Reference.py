from tkinter import *
from tkinter import ttk

class Plant:
    name = "Cabbage"

def printplant():
    print(Plant.name)

#Root is the root/main window of the application
root = Tk()
root.title("Main window")

#frm creates a frame widget, which in this case will hold a label and a button.
#The frame is fit inside the root window
frm = ttk.Frame(root, padding=10)
frm2 = ttk.Frame(root, padding=5)

#Specifies the frame to be a grid
frm.grid()

frm2.grid()

#Labels are used for text display
#You have to specify in which frame the label is supposed to go
ttk.Label(frm, text="hello world\nHow is it going?").grid(column=0, row=0)
ttk.Label(frm, text=Plant.name).grid(column=1, row=0)

#Buttons, same with the label where you have to specify which frame it needs to go it
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)

ttk.Button(frm2, text="Something", command=printplant()).grid(column=0, row=0)
root.mainloop()