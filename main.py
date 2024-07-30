from tkinter import *
from tkinter import ttk
from Plantclass import Plant
import pandas as pd

PlantDf = pd.read_csv("plantSpreadSheet.csv", delimiter=";")
PlantList = PlantDf['Plant'].tolist()

Cabbage = Plant(name="Cabbage",plantingMonth="June", sproutTime="4 weeks", growTime="2 months", additionalRemarks="Could pass a dict or list here")
Spinach = Plant(name="Spinach", plantingMonth="August", sproutTime="3 weeks", growTime="3 months", additionalRemarks="Some info")

main = Tk()
main.title("PlantManager")
#First frame
frm1 = ttk.Frame(main, padding=10)
frm1.grid()
#Second frame
frm2 = ttk.Frame(main, padding=10)
frm2.grid()

frm3 = ttk.Frame(main, padding=10)
frm3.grid()

#ttk.Label(frm1, text=Cabbage.additionalRemarks).grid(column=0, row=0)

#this function works but places the properties in a weird order
def plantLabel(plant, tkinterFrame):
    j = 0
    for i in plant.plantList():
        ttk.Label(tkinterFrame, text=i).grid(column=0, row=j)
        print(i)
        j += 1



plantLabel(Cabbage, frm1)
plantLabel(Spinach, frm2)



def addPlantWindow():
    addPlantWindow = Tk()
    addPlantWindow.title("Add Plant")
    #Creating frame and dropdown menu
    frmAddPlant = ttk.Frame(addPlantWindow, padding=10)
    frmAddPlant.grid()
    changedLabel = Label(frmAddPlant, text="Cabbage")
    changedLabel.grid(row=0, column=0)
    ttk.Button(frmAddPlant, text="Exit window", command=addPlantWindow.destroy).grid(column=0, row=1)
    ttk.Button(frmAddPlant, text="Save plant", command=addPlantWindow.destroy).grid(column=1, row=1)
    
    Selected = StringVar(addPlantWindow)
    Selected.set("Cabbage")

    drop = OptionMenu(addPlantWindow,Selected, *PlantList)
    drop.grid(row=0, column=2)

    def SelectedPlant():
        print(Selected.get())
        changedLabel["text"] = Selected.get()

    button = Button(addPlantWindow, text="Plant", command=SelectedPlant)
    button.grid(row=0,column=4)

    addPlantWindow.mainloop()



ttk.Button(frm1, text="New window", command=addPlantWindow).grid(column=0, row=0)

main.mainloop()