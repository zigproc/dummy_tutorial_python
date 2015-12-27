def count_to(count):
    """ Our iterator implementation """

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built in iterator
    # create a tuple such as (1,"eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through list
    for position, number in iterator:
        # return a generator
        yield number


for num in count_to(3):
    print("{}".format(num))

print("----")

for num in count_to(4):
    print("{}".format(num))
