from roman_numeral import convert_to_roman
from error import RomanNumeralError

def main():
    print("Convertisseur de Chiffres Arabes en Chiffres Romains")
    while True:
        input_str = input("Entrez un nombre (ou 'quit' pour quitter) : ")
        if input_str.lower() == 'quit':
            break
        try:
            number = int(input_str)
            roman = convert_to_roman(number)
            print(f"Le chiffre romain de {number} est {roman}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
        except RomanNumeralError as e:
            print(e)

if __name__ == "__main__":
    main()
