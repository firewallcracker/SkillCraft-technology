def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    
    choice = input("Enter your choice (1/2): ")
    
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return
    
    if choice == "1":
        encrypted = caesar_encrypt(message, shift)
        print(f"\nEncrypted text: {encrypted}")
    elif choice == "2":
        decrypted = caesar_decrypt(message, shift)
        print(f"\nDecrypted text: {decrypted}")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
