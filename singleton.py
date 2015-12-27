class Borg:
    """Borg class making class attributes global"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):
    """ This class shares all its attributes among its various instances """

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)

# create a singleton and add first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")

print(x)

y = Singleton(SNMP="Simple Network Management Protocol")

print(y)
