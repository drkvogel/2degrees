# -*- coding: utf-8 -*-

""" Convert lengths between different systems of units

* 6 m to yard = 6.562 yd
* 2.5 yd to inch = 90 in

units current supported are: metre (m), yard (yd) and inch (in)
result can be output as string, e.g., "2.3 m", "6 yd", "0.4 in"

"""

# class ConvertLength:
#     """ Contain functionality in a class?
#     """

# class Unit:
# units = [
#     ["Yard", "yd", 914.4],
#     ["Inch", "in", 25.4],
#     ["Metre", "m", 1000]
# ]

def __init__(self, name, abbr, mm_amount):
    self.name = name
    self.abbr = abbr
    self.mm = mm_amount
    return

def convert_length(in_unit, in_amount, out_unit, print_unit=False):
    """ Converts lengths between different systems of units

    Args:
        in_unit: The input unit
        in_amount: the input amount
        out_unit: The output unit
        print_unit: Whether to return the output as a string
        and include the unit

    Returns:
        A floating point number which is the result
        of the conversion in the units specified

    Raises:
        Exception: one or both of the units specified were not understood
        Exception: both of the units were the same
    """
    in_unit
    in_amount
    out_unit
    print_unit

    return

