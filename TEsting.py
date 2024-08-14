from tkinter import *
from tkinter import ttk
from Plantclass import Plant

root = Tk()

mainfrm = ttk.Frame(root, padding=20).grid()




Frame1 = ttk.Frame(mainfrm, padding=5)


#You have to seperate the assignment and the grid or else it doesnt work properly


nestedfrm1 = ttk.Frame(mainfrm, padding=10)
nestedfrm1.grid(row=0)
n1 = ttk.Label(nestedfrm1, text="nested frame 1")
n1.grid(row=0)
n2 = ttk.Label(nestedfrm1, text="nested frame 1.1")
n2.grid(row=1)
n3 = ttk.Label(nestedfrm1, text="nested frame 1.2")
n3.grid(row=2)


nestedfrm2 = ttk.Frame(mainfrm, padding=10)
nestedfrm2.grid(row=1)
n4 = ttk.Label(nestedfrm2, text="nested frame 2")
n4.grid(row=0)
n5 = ttk.Label(nestedfrm2, text="nested frame 2.1")
n5.grid(row=1)
n6 = ttk.Label(nestedfrm2, text="nested frame 2.2")
n6.grid(row=2)

root.mainloop()