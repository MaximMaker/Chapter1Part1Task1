def is_even(number):
    if number % 2 == 0:
        print("Even!")
        return True
    else:
        print("Odd!")
        return False

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(8) == True
    assert is_even(100) == True
    assert is_even(101) == False

test_is_even()