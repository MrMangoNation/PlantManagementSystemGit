from tkinter import *
from tkinter import ttk

main =Tk()
mainFrame = ttk.Frame(main, padding=10).grid()
Cabbage = ttk.Frame(mainFrame, padding=10).grid()

#Theoretically works, just is not very pretty
ttk.Label(Cabbage, text="Location").grid(column=0, columnspan=2, row=0)
ttk.Label(Cabbage, text="Cabbage").grid(column=0, columnspan=2, row=1)
ttk.Label(Cabbage, text="planting month").grid(column=0, row=2)
ttk.Label(Cabbage, text="harvest month").grid(column=1, row=2)
ttk.Label(Cabbage, text="sprout time").grid(column=0, row=3)
ttk.Label(Cabbage, text="transplant time").grid(column=1, row=3)
ttk.Label(Cabbage, text="frm creates a frame widget, which in this case will hold a label and a button.", wraplength=100).grid(column=2, row=0, rowspan=4)



ttk.Button(mainFrame, text="Quit", command=main.destroy).grid(column=0, row=9)


main.mainloop()