class RomanNumeralError(Exception):
    def __init__(self, code=None):
        if code == "ZERO":
            message = "Le chiffre 0 n'existe pas en chiffres romains"
        elif code == "NEGATIVE":
            message = "Les nombres négatifs ne peuvent pas être convertis en chiffres romains"
        elif code == "NON_INTEGER":
            message = "Seuls les nombres entiers peuvent être convertis en chiffres romains"
        elif code =="TOO_BIG":
            message = "Le nombre est trop grand pour être convertis en chiffre romains (Maximum 3999)"
        else:
            message = "Erreur lors de la conversion en chiffre romain"
        
        super().__init__(message)
