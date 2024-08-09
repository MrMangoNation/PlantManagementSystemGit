from tkinter import *
from tkinter import ttk
from Plantclass import Plant

root = Tk()

mainfrm = ttk.Frame(root, padding=20).grid()






nestedfrm1 = ttk.Frame(mainfrm, padding=10).grid(row=0)
ttk.Label(nestedfrm1, text="nested frame 1").grid(column=0, row=0)
ttk.Label(nestedfrm1, text="nested frame 1.1").grid(column=0, row=1)
ttk.Label(nestedfrm1, text="nested frame 1.2").grid(column=0, row=2)
ttk.Label(nestedfrm1, text="nested frame col1row2").grid(column=0, row=2)
ttk.Label(nestedfrm1, text="nested frame 1.3").grid(column=0, row=3)
ttk.Label(nestedfrm1, text="nested frame col1row3").grid(column=0, row=3)

nestedfrm2 = ttk.Frame(mainfrm, padding=10).grid(row=1)
ttk.Label(nestedfrm2, text="nested frame 2").grid(column=0, row=0)
ttk.Label(nestedfrm2, text="nested frame 2.1").grid(column=0, row=1)
ttk.Label(nestedfrm2, text="nested frame 2.2").grid(column=0, row=2)
ttk.Label(nestedfrm2, text="nested frame 2 col1row2").grid(column=0, row=2)
ttk.Label(nestedfrm2, text="nested frame 2.3").grid(column=0, row=3)
ttk.Label(nestedfrm2, text="nested frame 2 col1row3").grid(column=0, row=3)



nestedfrm3 = ttk.Frame(mainfrm, padding=10).grid(row=2)
ttk.Label(nestedfrm3, text="nested frame 3").grid()



root.mainloop()