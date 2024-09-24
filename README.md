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


Plants system

Mock up:

Plant box:
Name of plant/crop/herb
Location
Date planted
Aprox. Date for harvest
Special notes


There’ll be 2 different CSV files
1 which functions as a database that contains the data for all the plants and cultivars
The second one will be used to keep track of the planted plants, when they’ve been planted and where

Find a way to communicate between the GUI and the CSV file database, to lookup the name of the plant in the database and pull the needed properties from the plant


PlantClass:
This class will only be used to store data about a plant, such as its species, its best planting month etc.
This is more akin to a database, but done in CSV cuz I don’t know how to work with a database
- Plant name
    - Type of plant/cultivar
- Best month to plant
- Time it takes to sprout
- Time it takes to grow/harvest from point of planting
- Additional remarks that might be useful to know


Using the CSV file to save, modify and move data between sessions
What data do we want stored in the CSV file?
- Plant (plantName)
    - Type of plant/cultivar (optional)
- Date planted
    - From the date planted, also generate when approximately the plant would be ready for harvest
        - This can be done with the tkinter calendar package
        - Have to figure out a way to work with dates
- Location planted
- Through the systemn allow for projected growth time, and harvest time from the database file
Once we have this data, we need to write it to the CSV file
One way to do this is with pandas and a DataFrame
Load the CSV as a pandas dataframe, edit it and afterwards save it back to the CSV
Later we can read from this CSV to display which plants are planted where
Find a way to allow the user to set a predetermined size of the plant box/hydroponics system


Next steps:
- Data preservation between sessions
    - Come up with a way to save the currently planted plants, and be able to load and read from this file and modify it.
    - Currently the plan is to use a CSV to save and edit the currently planted plants.
        - Use a tk window to display the plants form the CSV file
        - Find a way to edit the CSV with an entry window for the plants
        - Could load the CSV with pandas, change the data frame and then write the data frame back to the CSV
- Plant list with information about plants herbs and other things that I can plant.
    - This can be done with a database maybe, since it does not need a lot of modifaction

For plant frame
- Can use a list with all the plant names, using a CSV file
Create the frames before the function, with a while loop, stopping when the last plant has been hit
Then create the labels for the plant with a function and a for loop, printing each property of the class to the frame


How to find a plant in the CSV through the GUI?
- Once the CSV has been loaded as a dataframe in pandas, then we can lookup the name of the plant in the dataframe
- Once found we can pull the needed properties from the dataframe, and display it in the GUI
