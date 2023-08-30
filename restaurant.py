#restaurant initialised with name as a string.
from review import Review
from customer import Customer
class Restaurant:
    def __init__(self, name):
        self._name = name
        self.reviews = []


    # def getreviews(self):
    #     return self.reviews

    # def setreviews(self, review):
    #     print(review.restaurant().name())
    #     print("Tumefika")
    #     self.reviews.append(review)
    #     print(self.reviews)

    # reviews = property(getreviews,setreviews)

 #returns name.       
    def name(self):
        return self._name

 #adding review.
    def add_review(self, customer, rating):
        Review(customer,self,rating)
        # self.reviews.append(review)

#calculating average rating.  
    def average_star_rating(self):
        if len(self.reviews) == 0:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews])

        avg_rating = total_ratings / len(self.reviews)
        return avg_rating

#review class for customer reviews
# class Review:
#     def __init__(self, customer, rating):
#         self._customer = customer
#         self._rating = rating

#  #accessing rating attribute as a property.   
#     @property
#     def rating(self):
#         return self._rating\

# restaurant1.add_review(Review("Customer X", 5))
# restaurant1.add_review(Review("Customer Y", 5))
# restaurant1.add_review(Review("Customer Z", 3))

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

customer1 = Customer("George", "Washington")
restaurant1.add_review(customer1,9)
# print(Review.allreviews)


# restaurant1 = Restaurant("Hilton Hotel")
print("Restaurant name:", restaurant1.name())

print("Average rating:", restaurant1.average_star_rating())


# restaurant2 = Restaurant("Weston Hotel")
print("Restaurant name:", restaurant2.name())

# restaurant2.add_review(Review("Customer X", 5))
# restaurant2.add_review(Review("Customer Y", 2))
# restaurant2.add_review(Review("Customer Z", 3))

print("Average rating:", restaurant2.average_star_rating())

# restaurant3 = Restaurant("Weston Hotel")
print("Restaurant name:", restaurant3.name())

# restaurant3.add_review(Review("Customer X", 3))
# restaurant3.add_review(Review("Customer Y", 4))
# restaurant3.add_review(Review("Customer Z", 3))

print("Average rating:", restaurant3.average_star_rating())

#printing all reviews
print("\nAll Reviews:")
for review in Review.all():
    # print(review.restaurant())
    # customer = review.customer().given_name()
    # restaurant = review.restaurant().name()
    # l_name = 
    # print(f"Customer: {}, Restaurant: {}, Rating: {review.rating()}")
    print(f"Customer: {review.customer().given_name()}, Restaurant: {review.restaurant().name()}, Rating: {review.rating()}")
