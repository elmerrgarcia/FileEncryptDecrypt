import pyfiglet
import os
from cryptography.fernet import Fernet


def display_menu():

    # Clear terminal for a clean look
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create the ASCII banner
    banner = pyfiglet.figlet_format("File Encryptor / Decryptor", font="slant")
    print(banner)
    print("-" * 50)
    print("1. Encrypt a File")
    print("2. Decrypt a File")
    print("3. Generate/Check Key")
    print("4. Exit")
    print("-" * 50)


def load_key():
    if not os.path.exists("secret.key"):
        return None
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key):
    """
    Given a filename and a key, decrypts the file and
    overwrites it with the original data.
    """
    f = Fernet(key)

    # 1. Read the encrypted bytes
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    try:
        # 2. Attempt to decrypt
        decrypted_data = f.decrypt(encrypted_data)

        # 3. Write the original data back to the file
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        print(f"Successfully decrypted {filename}")

    except Exception as e:
        print("Decryption Failed: Invalid key or corrupted file.")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice in ['1', '2']:
            key = load_key()
            if not key:
                print("❌ No 'secret.key' found! Generate one first (Option 3).")
            else:
                filename = input("Enter filename: ")
                if os.path.exists(filename):
                    if choice == '1':
                        encrypt_file(filename, key)
                    else:
                        decrypt_file(filename, key)
                else:
                    print("❌ File not found.")
            input("\nPress Enter...")

        elif choice == '3':
            if os.path.exists("secret.key"):
                print("⚠️  'secret.key' already exists!")
                confirm = input("Overwrite it? (This will make old files unreadable!) y/n: ")
                if confirm.lower() != 'y':
                    input("Action cancelled. Press Enter...")
                    continue

            key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(key)
            print("✅ New key generated and saved to 'secret.key'.")
            input("Press Enter...")

        elif choice == '4':
            break

if __name__ == "__main__":
    main()
