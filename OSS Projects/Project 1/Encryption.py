def main() :
    print("Caesar Cipher Cracker (Harry Derderian)")
    print("="*50)
    ENCRYPTED_STR = input("Input caesar cipher text: ").upper()
    for string in bruteForce(ENCRYPTED_STR) :
          print(string)

def bruteForce(cipher_str) -> list[str]:
        SPACE_ASCII_DECIMAL = 32
        LAST_ALPHA_ASCII_DECIMAL = 90
        possible_variants = []
        current_attempt = ""
        for shift_amount in range (1, 26) :
            for char in cipher_str :
                    char_ascii_decimal = ord(char) + shift_amount
                    if char_ascii_decimal > LAST_ALPHA_ASCII_DECIMAL :
                        current_attempt += chr( (char_ascii_decimal % 90) + 64)
                    elif char_ascii_decimal - shift_amount == SPACE_ASCII_DECIMAL :
                          current_attempt += ' '
                    else :
                          current_attempt += chr(char_ascii_decimal)
            possible_variants.append(current_attempt)
            current_attempt = ""
        return possible_variants
main()