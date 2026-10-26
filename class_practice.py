class Dog:
    def __init__(self, name):     # runs once, when the object is created
        self.name = name          # store data INSIDE the object

    def bark(self):               # a function that belongs to the object
        print(f"{self.name} says woof!")

    def sit(self):
        print(f"{self.name} sits.")


rex = Dog("Rex")
max_dog = Dog("Max")
rex.bark()       # self = rex     → "Rex says woof!"
max_dog.bark()   # self = max_dog → "Max says woof!"

rex.sit()
max_dog.sit()