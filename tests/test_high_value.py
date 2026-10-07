from lib.high_value import *


"""
Check if value_first and value_second is an integer
"""
def test_check_value_first_return_int():
    values = HighValue(8, 4)
    is_first_value_int = isinstance(values.value_first, int)
    assert is_first_value_int == True


def test_check_value_second_return_int():
    values = HighValue(8, 4)
    is_second_value_int = isinstance(values.value_second, int)
    assert is_second_value_int == True

"""
Check "First value is higher" returns when value_first 
is greater than value_second
"""

def test_check_first_value_returns_first_value_when_greater_than_second_value():
    values = HighValue(8, 4)
    result = values.get_highest()
    assert result == "First value is higher"

"""
Check "Second value is higher" returns when value_first 
is less than value_second
"""

def test_check_second_value_return_second_value_when_greater_than_first_value():
    values = HighValue(3, 9)
    result = values.get_highest()
    assert result == "Second value is higher"

"""
Check "Values are equal" returns when value_first 
and value_second are the same
"""

"""
Check value_first has increased when the selection
for add is "first"
"""

"""
Check value_second has increased when the selection
for add is "second"
"""

"""
Check value_first has decreased when the selection
for add is "first" and the number is negative
"""

"""
Check value_second has decreased when the selection
for add is "second" and the number is negative
"""