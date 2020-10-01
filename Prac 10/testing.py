"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s for i in range(0, n)])



def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length



def run_tests():
    """Run the tests on the functions."""

    assert repeat_string("Python", 1) == "Python"

    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0, "Car does not set fuel correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"


run_tests()

doctest.testmod()

def format_sentence(phrase):
    phrase = phrase.split()
    phrase [0] = phrase[0].title()
    if len(phrase) > 1:
        count = 0
        for i in range(0, len(phrase)-1):
            count += 1
            phrase.insert(i+count, " ")
    phrase.append(".")
    return "".join(phrase)


assert format_sentence("hello") == "Hello."

assert format_sentence("It is an ex parrot") == "It is an ex parrot."

assert format_sentence("New Playstation is coming") == "New Playstation is coming."


