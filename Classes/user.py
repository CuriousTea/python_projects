class Users:

    def __init__(self, first_name, last_name, pokemon_type):
        self.first_name = first_name
        self.last_name = last_name
        self.pokemon_type = pokemon_type
    def describe_user(self):
        print("First Name " + self.first_name)
        print("Last Name " + self.last_name)
        print("Pokemon Type: " + self.pokemon_type)
    def greet_user(self):
        print(f"Hello, {self.first_name}")

joe = Users('Joe','Rogan','Fighting')

joe.greet_user()
joe.describe_user()

