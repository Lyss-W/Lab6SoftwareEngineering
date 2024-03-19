# Alyssa Williams
def encoder(num):
    encoded_digits = []
    for digit in num:
        digit = int(digit) + 3
        if digit > 9:
            digit -= 10
        digit = str(digit)
        encoded_digits.extend(digit)
    return ''.join(encoded_digits)