"""higher-order function is a function that takes a function as an argument value or returns a function as a return value, This is a example to dispaly the latter. """
def make_adder(n):
    """Return a function that takes one argument K and return K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
