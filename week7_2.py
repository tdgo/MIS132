# MIS 132 - May 7
# Animal - Dog - Cat Clases

class Animal:
    def __init__(self, name):
        self.name = name
        #print("Hey! It is an animal object.")

    def greet(self):
        print("Hi!")

    def who_am_i(self):
        print("Animal")

    def speak(self):
        print("Hi! How you doing?")


class Dog(Animal):

    def __init__(self,name):
        Animal.__init__(self,name)
        #print("Hey! It's also a dog.")

    def speak(self):
        print("Hav! Hav!")

    def who_am_i(self):
        return f"I'm {self.name}."


class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

    def speak(self):
        print("Meow! Meow!")


fox = Dog("Fox")
#fox.speak()
#print(type(fox))

boncuk = Cat("Boncuk")
#boncuk.speak()
#print(type(boncuk))

my_pets = (fox, boncuk)

for pet in my_pets:
    pet.speak()




