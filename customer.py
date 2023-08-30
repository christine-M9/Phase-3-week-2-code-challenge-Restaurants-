#customer initialised with given name and family name.
from review import Review
class Customer:
    all_customers = []
    
    def __init__(self, name, family_name):
        self._name = name
        self._family_name_given = family_name
        self._reviews = []
        Customer.all_customers.append(self)

#returns given name      
    def given_name(self):
        return self._name

#changes given name.
    def change_given_name(self, new_given_name):
        self._name = new_given_name

#returns family name.
    def get_family_name(self):
        return self._family_name_given

#changes after customer is created.
    def change_family_name(self, new_family_name):
        self._family_name_given = new_family_name

#customer's fullname.
    def full_name(self):
        return f"{self._name} {self._family_name_given}"

#calculating number of reviews associted with customer.
    def num_reviews(self):
        return len(self._reviews)

#class method to find customer by their full name.
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None
#class method to find all customers with a given name
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer._name == name:
                matching_customers.append(customer)
        return matching_customers
    
#property method to get the family name of a customer
    @property
    def family_name(self):
        return self._family_name_given

#setter method for updating the family name of a customer
    @family_name.setter
    def family_name(self, new_family_name):
        self._family_name_given = new_family_name

# Class method to retrieve all customers
    @classmethod
    def all(cls):
        return cls.all_customers

#review class to store customer reviews
# class Review:
#     all_reviews = []
    
#     def __init__(self, customer, restaurant, rating):
#         self._customer = customer
#         self._restaurant = restaurant
#         self._rating = rating
#         Review.all_reviews.append(self)

# Creating a customer
customer1 = Customer("George", "Washington")
print(customer1.given_name())
print(customer1.full_name())

customer1.change_given_name("Christine")
print(customer1.given_name())

# Change family name using property
customer1.family_name = "Juma"
print(customer1.family_name)
print(customer1.full_name())

# Printing all customers
print("\nAll Customers:")
for customer in Customer.all():
    print(customer.full_name())
