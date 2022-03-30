import Prgm1
import pytest
@pytest.mark.xfail
@pytest.mark.paramertize("number, result",[(153, True),(231,False)])
def test_armstrong(number, result):
    Armstrong = Prgm1.armstrong(number)
    assert Armstrong == result

@pytest.mark.skip(reason="no need")
@pytest.mark.parametrize("number, result",[(8, True),(10, False)])
def test_divisibleBy8(number, result):
    DivisibleBy8 = Prgm1.divisible_8(number)
    assert DivisibleBy8 == result

@pytest.mark.xfail
@pytest.mark.parametrize("number1, number2, number3, result",[(1,2,3,1),(2,3,4,5)])
def test_Smallest(number1, number2, number3, result):
    Smallest = Prgm1.smallest_3numbers(number1, number2, number3)
    assert Smallest == result

@pytest.mark.xfail
@pytest.mark.parametrize("number, result",[(1,"odd"),(2,"even"),(3,"even")])
def test_EvenOrOdd(number, result):
    EvenOrOdd = Prgm1.even_or_odd(number)
    assert EvenOrOdd == result

@pytest.mark.xfail
@pytest.mark.parametrize("number, result",[("moon", False),("malayalam", True)])
def test_Palindrome(number, result):
    IsPalindrome = Prgm1.is_palindrome(number)
    assert IsPalindrome == result




