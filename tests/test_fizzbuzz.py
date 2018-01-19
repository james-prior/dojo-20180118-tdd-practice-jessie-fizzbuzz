import pytest

from fizzbuzz import Fizzbuzz

number_to_expected_value = {
    1: (1,),
    # 30: (1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz'...'fizzbuzz'),
    # 2: 2,
    # 5: 'buzz',
    # 3: 'fizz',
    # 7: 7,
    # 15: 'fizzbuzz',
    # 23: 23,
    # 101: 101,
    # 102: 'fizz',
    # 20: 'buzz',
}
@pytest.mark.parametrize('max_number, expected_value', number_to_expected_value.items())
def test_known_number_returns_expected(max_number, expected_value):
    fb = Fizzbuzz(max_number)
    assert expected_value == fb.all()
