from tkinter import *
from tkinter import ttk
from Plantclass import Plant

Cabbage = Plant(name="Cabbage",location="PlantBox", plantingMonth="June", sproutTime="4 weeks", growTime="2 months", additionalRemarks="Could pass a dict or list here")

main =Tk()
mainFrame = ttk.Frame(main, padding=10).grid()
CabbageFrm = ttk.Frame(mainFrame, padding=10).grid(row=0)



#Theoretically works, just is not very pretty
#This function creates all the text needed from the plant class
#Does not create the frame, need to find a way to create a frame then have the frame name be the same name as the plant
def CreatePlantFrame(passedPlant, passedFrame):
    print(passedPlant.name)
    ttk.Label(passedFrame, text=passedPlant.location).grid(column=0, columnspan=2, row=0)
    ttk.Label(passedFrame, text=passedPlant.name).grid(column=0, columnspan=2, row=1)
    ttk.Label(passedFrame, text=passedPlant.plantingMonth).grid(column=0, row=2)
    ttk.Label(passedFrame, text=passedPlant.growTime).grid(column=1, row=2)
    ttk.Label(passedFrame, text=passedPlant.sproutTime).grid(column=0, row=3)
    ttk.Label(passedFrame, text="transplant time").grid(column=1, row=3)
    ttk.Label(passedFrame, text=passedPlant.additionalRemarks, wraplength=100).grid(column=2, row=0, rowspan=4)

CreatePlantFrame(Cabbage, CabbageFrm)


ttk.Button(mainFrame, text="Quit", command=main.destroy).grid(column=0, row=9)


main.mainloop()