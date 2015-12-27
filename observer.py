class Subject(object): #represents what is being observed

    def __init__(self):
        self._observers = []  # One to many relationship

    def attach(self, observer):
        # append observer to list if not already
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0  # Initialize temp of core

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp

        # Notify observers
        self.notify()


class TempViewer:

    def update(self, subject):  # Alert method
        print("Temperature Viewer: {} has temperature {}").format(subject._name, subject._temp)

# create subjects
c1 = Core("core1")
c2 = Core("core2")

# create observers
v1 = TempViewer()
v2 = TempViewer()

# attach observers to first core
c1.attach(v1)
c1.attach(v2)

# Change temp of first core
c1.temp = 80
c1.temp = 90
