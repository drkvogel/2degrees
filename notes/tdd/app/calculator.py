
class Calculator(object):

    def add(self, x, y):
        number_types = (int, float, long, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y    # was pass

            #import pdb; pdb.set_trace()

            # result = x - y  # deliberately wrong to fail test
            # print 'X is: {}'.format(x)
            # print 'Y is: {}'.format(y)
            # print 'Result is: {}'.format(result)
        else:
            raise ValueError
