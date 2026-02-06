class Animal:
    def sound(self):
        return "Some generic sound"
    
class Dog(Animal):
    def sound (self):
        return "WOOF WOOOOFFFF"
    
class Cat(Animal):
    def sound(self):
        return "MEEOOOOOOOOWWWWWWWWWWWWWWWWW"
    
animals = [Dog(),Cat(), Animal()]
for animal in animals:
    print (animal.sound())