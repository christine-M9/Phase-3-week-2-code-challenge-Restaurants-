#restaurant initialised with name as a string.
class Restaurant:
    def __init__(self, name):
        self._name = name
#returns name        
    def name(self):
        return self._name

    
restaurant1 = Restaurant("Ceejay Inn")
print(restaurant1.name())  





