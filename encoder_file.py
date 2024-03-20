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

#Shohruh Ismatulla
def decoder(num_string):
    decoded_string = ""
    for number in num_string:
        num = int(number) - 3
        if num < 0:
            num += 10
        decoded_string += str(num)
    return decoded_string