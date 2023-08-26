from customer import Customer
from restaurant import Restaurant
#iniatializing 
class Review:
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
#returns rating number       
    def rating(self):
        return self.rating_number



#Creating customer and restaurant
customer1 = Customer("Mathews", "Juma")
restaurant1 = Restaurant("Hilton Hotel")

#Creating a review 
review1 = Review(customer1, restaurant1, 8)

#Accessing the review's attributes
print("Customer:", review1.customer.given_name())
print("Restaurant:", review1.restaurant.name())
print("Rating:", review1.rating)



