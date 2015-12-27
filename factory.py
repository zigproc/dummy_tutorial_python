class Cat:

    """ Simple cat class """
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow"


class Dog:

    """ Simple dog class """
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


def get_pet(pet="dog"):
    """Factory method to create objects"""

    pets = dict(dog=Dog("Fido"), cat=Cat("Claude"))

    return pets[pet]

d = get_pet("cat")
print(d.speak())
