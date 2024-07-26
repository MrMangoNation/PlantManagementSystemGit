from tkinter import *

#Creates main window
root = Tk()

#Function to show the selected item in the dropdown menu
#The label text gets changed 
def show():
    label.config(text = clicked.get())

#List for the dropdown menu
options = [ 
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
]

#Defines the clicked variable to be a StringVariable
clicked = StringVar()

#Set method sets the value of the StringVariable to specified value
clicked.set("Monday")

#Creates the dropdown/OptionMenu object
#The * makes it so the options list gets handled as a list, if this gets removed then the entire list gets put in as a single option
#It has a parameter "clicked" which is the variable created earlier, the value of the dropdown menu gets written to this variable
drop = OptionMenu(root,clicked, *options)

#pack is a method that shows the object
drop.pack()

#Creates a button, that uses the function created earlier to print the selected option in the label
button = Button(root,text="clickme",command=show).pack()

#Creates the label with no text
label=Label(root,text="")

#Renders the label
label.pack()

#starts the program
root.mainloop()