class Korean:
    """ Korean speaker """

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """ English speaker """

    def __init__(self):
        self.name = "English"

    def speak_english(self):
        return "Hello"


class Adapter:
    """ This changes the generic method name to individaul method names """

    def __init__(self, object, **adapted_method):
        """ Change the name of the method """

        self._object = object

        """ Add new dictionary item to establish mapping """
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """ Return the rest of the attributes """
        return getattr(self._object, attr)


# list to store speaker objects
objects = []

# create a Korean object
korean = Korean()

# create the British object
british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says {}".format(obj.name, obj.speak()))
