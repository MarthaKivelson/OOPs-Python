
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a generic sound")

class Dog(Animal):
    def __init__(self, name):
        self.behaviour = "friendly"

    def speak1(self):
        print(f"{self.name} barks")
        print(f"{self.name} is {self.behaviour}")

anml = Animal("Generic animal")
anml.speak()

bow = Dog("Bow")
bow.speak()
bow.speak1()'''



#method overriding & overloading
'''class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a generic sound")

class Dog(Animal):
    # def __init__(self, breed):
    #     super().__init__()
    #     self.breed = breed

    def speak1(self):
        print(f"{self.name} barks")
        print(f"{self.name} is {self.breed}")

anml = Animal("Generic animal")
anml.speak()

bow = Dog("Bow")
bow.speak()
bow.speak1()'''

#super
class Animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks")
        print(f"{self.name} is {self.breed}")

# anml = Animal()
# anml.speak()

bow = Dog("Pug")
bow.speak()
