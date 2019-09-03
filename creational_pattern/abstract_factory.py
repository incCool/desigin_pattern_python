"""
@author: inc
"""

import random


class PetShop:
    """A PET SHop"""

    def __init__(self, animal_factory=None):
        """
        pet abstract factory
        :param animal_factory:
        """
        self.pet_animal = animal_factory

    def show_pet(self):
        """
        Creates and shows a pet usign abstract_factory
        :return:
        """

        pet = self.pet_animal.get_pet()
        print("pet: {}".format(pet))
        print("pet speak: {}".format(pet.speak()))


# factory create objects
class Dog:
    def speak(self):
        return "dog: woof! woof!"

    def __str__(self):
        return "Dog hi"


class Cat:
    def speak(self):
        return "miao miao miao!"

    def __str__(self):
        return "cat hi"


# factory classs
class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


# Create
def get_factory():
    """ dynamic """
    return random.choice([DogFactory, CatFactory])()


if __name__ == '__main__':
    shop = PetShop()
    for i in range(4):
        shop.pet_animal = get_factory()
        shop.show_pet()
        print("*"*20)
