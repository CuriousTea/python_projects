class Restaurant: 

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 

    def describe_restaurant(self):
            print("Name: " + self.restaurant_name)
            print("Cuisine: " + self.cuisine_type)
            
    def open_restaurant(self):
            print("The restaurant is open")

my_restaurant = Restaurant('Disciplne','Availability Heuristic')
print(f"{my_restaurant.restaurant_name}")
print(f"{my_restaurant.cuisine_type}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

