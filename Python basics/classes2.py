
class Mammals:
    def walk(self):
        print("WALK")


class Dog(Mammals):
    def bark(self):
        print("BARK")


class Cat(Mammals):
    def be_annoying(self):
        print("ANNOYING")


cat1 = Cat()
cat1.be_annoying()
cat1.walk()
