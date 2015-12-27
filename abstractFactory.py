class Dog:

    """ Simple dog class """
    def __str__(self):
        return "Dog"

    def speak(self):
        return "Woof!"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Return a Dog object"""
        return Dog()

    def get_food(self):
        """Return a dog food object """
        return "Dog Food"


class PetStore:
    """Petstore houses abstract factory"""

    def __init__(self, pet_factory=None):
        """ pet factory is abstract factory """

        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility to display details of object """

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("It's food is '{}'".format(pet_food))

# create a concrete factory

factory = DogFactory()

# create a pet store housing abstract factory
shop = PetStore(factory)

# Invoke utility
shop.show_pet()
