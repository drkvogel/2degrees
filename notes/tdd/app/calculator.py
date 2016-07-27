
class Calculator(object):

    def add(self, x, y):
        number_types = (int, float, long, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y    # was pass
        else:
            raise ValueError
