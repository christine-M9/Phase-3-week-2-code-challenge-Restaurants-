#restaurant initialised with name as a string.
class Restaurant:
    def __init__(self, name):
        self._name = name
        
#returns name.        
    def name(self):
        return self._name

#creating a restaurant.
restaurant1 = Restaurant("Hilton Hotel")
print(restaurant1.name())

#attempting to change the restaurant name.
restaurant1._name = "Weston Hotel"
print(restaurant1.name())



