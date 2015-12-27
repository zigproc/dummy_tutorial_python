class Component(object):
    """ Abstract class """

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    """ Concrete class """

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.name = args[0]

    def component_function(self):
        print("{}".format(self.name))


class Composite(Component):
    """ Concrete class, maintains the tree recursive structure """

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # store name of composite object
        self.name = args[0]

        # keep child items
        self.children = []

    def append_child(self, child):
        """ Method to add child item """
        self.children.append(child)

    def remove_child(self, child):
        """ Method to remove a child item """
        self.children.remove(child)

    def component_function(self):

        # print the name of the composite object
        print("{}".format(self.name))

        # iterate through and invoke component
        for i in self.children:
            i.component_function()


# build composite submenu 1
sub1 = Composite("submenu1")

# Create a new child sub submenu 11
sub11 = Child("sub_submenu 11")
sub12 = Child("sub_submenu 12")

sub1.append_child(sub11)
sub1.append_child(sub12)


# build top level composite
top = Composite("top_menu")

# build a submenu 2 that is not a composite
sub2 = Child("submenu2")

# add composite submenu1 to the top level
top.append_child(sub1)

# add composite submenu2 to the top level
top.append_child(sub2)

top.component_function()
