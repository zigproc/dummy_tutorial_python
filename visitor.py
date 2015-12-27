class House(object):  # class being visited
    def accept(self, visitor):
        """ Interface to accept a visitor """
        # Triggers the visiting operation
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print("{} worked on by {}".format(self, hvac_specialist))

    def work_on_electricity(self, electrician):
        print("{} worked on by {}".format(self, electrician))

    def __str__(self):
        """ return the class name """
        return self.__class__.__name__


class Visitor(object):
    """ Abstract visitor """
    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """ Concrete visitor """
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    """ Concrete visitor """
    def visit(self, house):
        house.work_on_electricity(self)

# Create an HVAC specialist
hv = HvacSpecialist()

# Create an electrician
e = Electrician()

# create a house
h = House()

# Let the house accept the HVAC specialist
h.accept(hv)

# Let the house accept the electrician
h.accept(e)
