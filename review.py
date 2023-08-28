from customer import Customer
from restaurant import Restaurant
#initializing
class Review:
    all_reviews = []
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)
        
    def customer(self):
        return self._customer
    
    def restaurant(self):
        return self._restaurant

#returns rating number   
    def rating(self):
        return self._rating
        
#returns all reviews.    
    @classmethod
    def all(cls):
        return cls.all_reviews

#creating customer and restaurant
customer1 = Customer("Mathews", "Juma")
customer2 = Customer("Christine", "Juma")
customer3 = Customer("James", "Mulwa")
restaurant1 = Restaurant("Hilton Hotel")
restaurant2 = Restaurant("Weston Hotel")
restaurant3 = Restaurant("Starbucks Hotel")

#creating reviews
review1 = Review(customer1, restaurant1, 8)
review2 = Review(customer2, restaurant2, 6)
review3 = Review(customer3, restaurant3, 7)

#accessing the review's attributes
print("Review Information:")
print("Customer:", review1.customer().given_name())
print("Restaurant:", review1.restaurant().name())
print("Rating:", review1.rating())

#printing all reviews
print("\nAll Reviews:")
for review in Review.all():
    print(f"Customer: {review.customer().given_name()}, Restaurant: {review.restaurant().name()}, Rating: {review.rating()}")
