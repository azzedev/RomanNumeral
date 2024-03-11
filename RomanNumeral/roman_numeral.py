from error import RomanNumeralError

def convert_to_roman(number):
    if (number==0):
        raise RomanNumeralError("ZERO")
    elif (number<0):
        raise RomanNumeralError("NEGATIVE")
    elif (number == float):
        raise RomanNumeralError("NON_INTEGER")
    elif (number >=4000):
        raise RomanNumeralError("TOO_BIG")
    
    roman_numerals = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
    roman_string =""
    
    for value in sorted(roman_numerals.keys(), reverse=True):
        while (number>=value):
            roman_string += roman_numerals[value]
            number-=value
    return roman_string