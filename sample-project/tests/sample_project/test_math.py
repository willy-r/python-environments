from sample_project.math import do_math


def test_do_math_one_plus_one_equal_two():
    assert do_math() == 2


def test_do_math_one_plus_one_not_equal_three():
    assert do_math() != 3
