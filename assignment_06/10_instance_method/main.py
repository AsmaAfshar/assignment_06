

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} says: miyaon miyaon!")
        
cat1 = Cat("Kitty", "Abyssinian")
cat1.bark()