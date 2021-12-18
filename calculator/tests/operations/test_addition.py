from ...operations import addition

def test_addition__sum_zero_values():
    result = addition()

    assert result == 0

def test_addition__sum_two_values():
    arg1 = 1
    arg2 = 2

    result = addition(arg1, arg2)

    assert result == 3

def test_addition__sum_three_values():
    arg1 = 1
    arg2 = 2
    arg3 = 3

    result = addition(arg1, arg2, arg3)

    assert result == 6
