class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = None

    def __str__(self):
        return f"I am {self.name} and I say {self.sound}"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Mieow"


class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Quack"


class PetShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def check_animals(self):
        for animal in self.animals:
            print(animal)


if __name__ == "__main__":
    shop = PetShop()
    shop.add_animal(Cat("Sylvester"))
    shop.add_animal(Dog("Pluto"))
    shop.add_animal(Duck("Donald"))

    shop.check_animals()
