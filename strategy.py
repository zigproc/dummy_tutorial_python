import types


class Strategy:
    """ Strategy pattern class """

    def __init__(self, function=None):
        self.name = "Default Strategy"

        if function is not None:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print("{} is used!".format(self.name))


# replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Create our default strategy
s0 = Strategy()
# Execute
s0.execute()

s1 = Strategy(strategy_one)
# Set name
s1.name = "Strategy 1"
# Execute
s1.execute()

s2 = Strategy(strategy_two)
# Set name
s2.name = "Strategy 2"
# Execute
s2.execute()



