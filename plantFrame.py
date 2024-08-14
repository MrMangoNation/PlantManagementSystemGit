from tkinter import *
from tkinter import ttk
from Plantclass import Plant

Cabbage = Plant(name="Cabbage",location="PlantBox", plantingMonth="June", sproutTime="4 weeks", growTime="2 months", additionalRemarks="Could pass a dict or list here")
Spinach = Plant(name="Spinach",location="PlantBox", plantingMonth="August", sproutTime="3 weeks", growTime="3 months", additionalRemarks="Some info")

main =Tk()
mainFrame = ttk.Frame(main, padding=10).grid()


#Theoretically works, just is not very pretty
#This function creates all the text needed from the plant class
#Does not create the frame, need to find a way to create a frame then have the frame name be the same name as the plant
#Can modify the function that it creates and returns a ttk frame
def CreatePlantFrame(passedPlant, rownumber):
    createdFrame = ttk.Frame(mainFrame, padding=10)
    createdFrame.grid(row=rownumber)
    print(passedPlant.name)
    l1 = ttk.Label(createdFrame, text=passedPlant.location)
    l1.grid(column=0, row=0)
    l2 = ttk.Label(createdFrame, text=passedPlant.name)
    l2.grid(column=0, row=1)
    l3 = ttk.Label(createdFrame, text=passedPlant.plantingMonth)
    l3.grid(column=0, row=2)
    l4 = ttk.Label(createdFrame, text=passedPlant.growTime)
    l4.grid(column=1, row=2)
    l5 = ttk.Label(createdFrame, text=passedPlant.sproutTime)
    l5.grid(column=0, row=3)
    l6 = ttk.Label(createdFrame, text="transplant time")
    l6.grid(column=1, row=3)
    #ttk.Label(createdFrame, text=passedPlant.additionalRemarks, wraplength=100).grid(column=2, row=0, rowspan=4)
    #Can make this function create and return the frame
    return createdFrame
CabbageFrame = CreatePlantFrame(Cabbage, 0)
SpinachFrame = CreatePlantFrame(Spinach, 1)

quitButton = ttk.Button(mainFrame, text="Quit", command=main.destroy)
quitButton.grid(column=0, row=2)

main.mainloop()