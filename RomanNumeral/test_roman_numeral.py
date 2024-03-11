import pytest
from roman_numeral import convert_to_roman
from error import RomanNumeralError


@pytest.mark.parametrize("number, expected", [
    (1, "I"),
    (5,"V"),
    (10,"X"),
    (50,"L"),
    (100,"C"),
    (500,"D"),
    (1000,"M"),

])

def test_convert_to_roman_classic(number, expected):
    assert convert_to_roman(number)==expected

@pytest.mark.parametrize("number, expected", [
    (4,"IV"),
    (9,"IX"),
    (40,"XL"),
    (90,"XC"),
    (400,"CD"),
    (900,"CM"),
])
def test_convert_to_roman_spe(number, expected):
    assert convert_to_roman(number)==expected

@pytest.mark.parametrize("number, expected", [
    (2,"II"),
    (3,"III"),
    (6,"VI"),
    (51,"LI"),
    (3000,"MMM"),
    (3999,"MMMCMXCIX"),

])
def test_convert_to_roman_add2(number, expected):
    assert convert_to_roman(number)==expected

@pytest.mark.parametrize("number", [
    0,
    4000,
    4001,
    -1,
    -4000

])
def test_convert_to_roman_error(number):
    with pytest.raises(RomanNumeralError):
        convert_to_roman(number)