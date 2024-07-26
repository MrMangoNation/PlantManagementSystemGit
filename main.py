from tkinter import *
from tkinter import ttk
from Plantclass import Plant

Cabbage = Plant(name="Cabbage",plantingMonth="June", sproutTime="4 weeks", growTime="2 months", additionalRemarks="Could pass a dict or list here")
Spinach = Plant(name="Spinach", plantingMonth="August", sproutTime="3 weeks", growTime="3 months", additionalRemarks="Some info")

main = Tk()
main.title("PlantManager")
#First frame
frm1 = ttk.Frame(main, padding=10)
frm1.grid()

frm2 = ttk.Frame(main, padding=10)
frm2.grid()

#ttk.Label(frm1, text=Cabbage.additionalRemarks).grid(column=0, row=0)

#this function works but places the properties in a weird order
def plantLabel(plantList, tkinterFrame):
    j = 0
    for i in Cabbage.plantList():
        ttk.Label(tkinterFrame, text=i).grid(column=0, row=j)
        print(i)
        j += 1
plantLabel(Cabbage, frm1)
plantLabel(Spinach, frm2)

main.mainloop()