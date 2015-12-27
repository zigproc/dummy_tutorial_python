from functools import wraps


def make_blink(function):
    """ Defines the decorator """

    # makes decorator transparent
    @wraps(function)
    # Define the inner function
    def decorator():
        # grab return value
        ret = function()

        return "<blink>" + ret + "</blink>"

    return decorator


@make_blink
def hello_world():
    """ Original Function """
    return "Hello, world"


# check result
print hello_world()


# check if function name is still same name
print(hello_world.__name__)

# check if function docstring is still the same
print(hello_world.__doc__)
