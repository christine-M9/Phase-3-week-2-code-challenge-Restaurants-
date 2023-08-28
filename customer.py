#customer initialised with given name and family name.
class Customer:
    all_customers = []
    
    def __init__(self, name, family_name):
        self._name = name
        self._family_name_given = family_name
        self._reviews = []
        Customer.all_customers.append(self)

#returns given name.       
    def given_name(self):
        return self._name

#changes given name.   
    def change_given_name(self, new_given_name):
        self._name = new_given_name

#returns family name.       
    def family_name(self):
        return self._family_name_given

#changes after customer is created.   
    def change_family_name(self, new_family_name):
        self._family_name_given = new_family_name

#customer's fullname.       
    def full_name(self):
        return f"{self._name} {self._family_name_given}"

#returns all customer instances.
    @classmethod
    def all(cls):
        return cls.all_customers

#creating a customer.
customer1 = Customer("George", "Washington")
print(customer1.given_name())
print(customer1.full_name())

customer1.change_given_name("Christine")
print(customer1.given_name())

customer1.change_family_name("Juma")
print(customer1.family_name())
print(customer1.full_name())

#printing all customer. 
print("\nAll Customers:")
for customer in Customer.all():
    print(customer.full_name())
