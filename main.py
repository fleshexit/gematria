from ciphers import Ciphers


def calculate_alphanumeric_qabbala_value(user_input):
    user_input = user_input.upper()  
    ciphers = Ciphers()
    ciphers.alphanumeric_qabbala() 

    value = 0
    for char in user_input:
        if char in ciphers.gematria:
            value += ciphers.gematria[char]

    return value

user_input = input("Enter a string: ")
result = calculate_alphanumeric_qabbala_value(user_input)
print(f"The alphanumeric qabbala value of '{user_input}' is: {result}")

