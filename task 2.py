import sys
from PIL import Image

def encrypt_image(input_path, output_path, key, mode="math"):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    if mode == "math":
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[i, j] = (r, g, b)

    elif mode == "swap":
        for i in range(width // 2):
            for j in range(height):
                opposite_x = width - i - 1
                pixels[i, j], pixels[opposite_x, j] = pixels[opposite_x, j], pixels[i, j]

    img.save(output_path)
    print(f"✅ Image encrypted ({mode} mode) and saved as {output_path}")

def decrypt_image(input_path, output_path, key, mode="math"):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    if mode == "math":
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[i, j] = (r, g, b)

    elif mode == "swap":
        for i in range(width // 2):
            for j in range(height):
                opposite_x = width - i - 1
                pixels[i, j], pixels[opposite_x, j] = pixels[opposite_x, j], pixels[i, j]

    img.save(output_path)
    print(f"✅ Image decrypted ({mode} mode) and saved as {output_path}")

def menu():
    print("=== Image Encrypt/Decrypt Menu ===")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ").strip()
    return choice

def get_image_params():
    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path: ").strip()
    key = int(input("Enter key (integer): ").strip())
    mode = input("Enter mode ('math' or 'swap'): ").strip().lower()
    return input_path, output_path, key, mode

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            print("\n--- Encrypt Image ---")
            input_path, output_path, key, mode = get_image_params()
            encrypt_image(input_path, output_path, key, mode)
        elif choice == "2":
            print("\n--- Decrypt Image ---")
            input_path, output_path, key, mode = get_image_params()
            decrypt_image(input_path, output_path, key, mode)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
