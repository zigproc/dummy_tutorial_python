import time


class Producer:
    """ Define the resource intensive object to instantiate """

    def product(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now")


class Proxy:
    """ Define the relatively less resource intensive object """

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """ Check if producer is available """
        print("Artist checking if Producer is available")

        if self.occupied == "No":
            # If available, create
            self.producer = Producer()
            time.sleep(2)

            self.producer.meet()
        else:
            # Otherwise don't instantiate
            time.sleep(2)
            print("Producer is busy")


# instantiate a proxy
p = Proxy()

# Make the proxy produce
p.produce()


p.occupied = "Yes"
p.produce()
