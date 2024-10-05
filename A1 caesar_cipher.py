def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using Caesar Cipher.
    
    :param text: The text to be encrypted or decrypted.
    :param shift: The number of positions to shift each letter.
    :param mode: 'encrypt' for encryption, 'decrypt' for decryption.
    :return: The encrypted or decrypted text.
    """
    result = []
    shift = shift % 26  # Ensure shift is within the range of 0-25
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)  # Non-alphabetic characters are not changed

    return ''.join(result)

def main():
    print("Welcome to the Caesar Cipher Program")
    
    # Input message
    message = input("Enter the message: ")
    
    # Input shift value
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. It must be an integer.")
        return
    
    # Encrypt
    encrypted_message = caesar_cipher(message, shift, mode='encrypt')
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt
    decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
    print(f"Decrypted message: {decrypted_message}")

if __name__ == '__main__':
    main()
