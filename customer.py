#customer initialised with given name and family name
class Customer:
    
    def __init__(self, name, family_name):
        self.name = name
        self.family_name_given = family_name
        
#returns given name
    def given_name(self):
        return self.name
#changes given name
    def change_given_name(self, new_given_name):
        self.name = new_given_name
#returns family name
    def family_name(self):
        return self.family_name_given
#changes after customer is created
    def change_family_name(self, new_family_name):       
        self.family_name_given = new_family_name
#customer's fullname        
    def full_name(self):
        return f"{self.name} {self.family_name_given}"  
        

customer1 = Customer("George", "Washington")
print(customer1.given_name())
print(customer1.full_name())

customer1.change_given_name("Christine")
print(customer1.given_name())

customer1.change_family_name("Juma")
print(customer1.family_name()) 
print(customer1.full_name())

