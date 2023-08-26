#customer initialised with given name and family name.
class Customer:
    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
#returns given name
    def given_name(self):
        return self.name
#changes given name 
    def change_given_name(self, new_given_name):
        self.name = new_given_name


customer1 = Customer("George", "Washington")
print(customer1.given_name()) 

customer1.change_given_name("Christine")
print(customer1.given_name())  
