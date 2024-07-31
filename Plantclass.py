"""
General plant class
This class will be used for every plant
It contains the following information per plant:
- Name, name of the plant/vegetable
- Best month of planting
- Sprout time, how long it takes to sprout
- Growth time, How long it takes to grow
- Additional remarks, stuff that might be usefull to know

Extra information besides this that can be added later
- Location of plant, where the plant is located, either in the grow box or in the hydro system

"""



class Plant:
    def __init__(self, name, location, plantingMonth, sproutTime, growTime, additionalRemarks):
        print('Class created')
        self.name = name
        self.location = location
        self.plantingMonth = plantingMonth
        self.sproutTime = sproutTime
        self.growTime = growTime
        self.additionalRemarks = additionalRemarks
    
    #Returns a list with all the attributes of the plant class    
    def plantList(self):
        return [self.name, self.plantingMonth, self.sproutTime, self.growTime, self.additionalRemarks]