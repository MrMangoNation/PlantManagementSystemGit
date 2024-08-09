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
    createdFrame = ttk.Frame(mainFrame, padding=10).grid(row=rownumber)
    print(passedPlant.name)
    ttk.Label(createdFrame, text=passedPlant.location).grid(column=0, row=0)
    ttk.Label(createdFrame, text=passedPlant.name).grid(column=0, row=1)
    ttk.Label(createdFrame, text=passedPlant.plantingMonth).grid(column=0, row=2)
    ttk.Label(createdFrame, text=passedPlant.growTime).grid(column=1, row=2)
    ttk.Label(createdFrame, text=passedPlant.sproutTime).grid(column=0, row=3)
    ttk.Label(createdFrame, text="transplant time").grid(column=1, row=3)
    #ttk.Label(createdFrame, text=passedPlant.additionalRemarks, wraplength=100).grid(column=2, row=0, rowspan=4)
    #Can make this function create and return the frame
    return createdFrame
CabbageFrame = CreatePlantFrame(Cabbage, 0)
SpinachFrame = CreatePlantFrame(Spinach, 10)

ttk.Button(mainFrame, text="Quit", command=main.destroy).grid(column=0, row=9)


main.mainloop()