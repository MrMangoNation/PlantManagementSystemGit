This program is made for maintaining and planning for plants

The objective of this program is as follows:
Allow a user to easily track when plants are planted and their projected growth and harvest times/dates


There are 3 layers to this program:
- Database for plants that can be editted which contains general information about plants
- A way to track when which plants are planted, and be able to have a projected growth and harvest time
- GUI which tracks plant growth, and where growth can be logged

Database:
- Contains general information of the plant, such as projected growth time, harvest time and additional remarks to keep track of
- Can be edited easily, to add or remove plants or cultivars
- The database is used in the GUI of the program as well to help the user plan their planting

Plant tracking:
- Allows the user to input when plants were planted
- When plants are added, calculate projected growth and harvest time
- Allow for restructuring and removal of plants when harvested

GUI:
- The main part of the program which shows all the information for the user regarding planted plants, information about the plants, projected growth and harvesting times
- This will exist out of several windows using Tkinter allowing the user to add plants, remove plants, have the planted plants show in a nice overview
- The main objective is to allow the user to easily change plants, and show a nice overview of what is planted
  

More in-depth of each module:

Database:
This will consist of a CSV file containing a wide variety of plants with important information pertaining to them including growth time, harvest time, best month to plant in, and any additional remarks
The CSV file will likely not be eddited much outside of adding new plants or cultivars when they are purchased.
From this database a couple of things will need be read at certain points in the program:
- When the user wants to add a planted plant, they will need to have the option to choose from the plants in the database
- When the user wants to garner information about plants, they will need to be able to choose from the plants in the databse

Plant tracking:
This module will also have a CSV as a centerpiece. With this CSV the user will be able to track which plants are planted where.
The CSV will work as a database keeping track of everything, and allowing it to be displayed with Tkinter, and allow the user to interact with the information from the CSV.
This CSV will be both read from and written to a lot.


