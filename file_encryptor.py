# python
import os
import hashlib


def generate_key(password: str) -> bytes:
    """Generate a 32-byte key using SHA-256 from the given password."""
    return hashlib.sha256(password.encode()).digest()


def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    """Encrypt or decrypt data using XOR with the given key."""
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])


def encrypt_file(file_path: str, password: str) -> None:
    """Encrypt the file at the given path."""
    key = generate_key(password)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = xor_encrypt_decrypt(data, key)

    # save encrypted data back to the file
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"File '{file_path}' has been encrypted.")


def decrypt_file(file_path: str, password: str) -> None:
    """Decrypt the file at the given path."""
    key = generate_key(password)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = xor_encrypt_decrypt(encrypted_data, key)

    # save decrypted data back to the file
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"File '{file_path}' has been decrypted.")


def main():
    print("File Encryptor/Decryptor")
    file_path = input("Enter the file path: ")
    password = input("Enter a password: ")
    action = input("Do you want to (e)ncrypt or (d)ecrypt the file? ").lower()

    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return

    if action == "e":
        encrypt_file(file_path, password)
    elif action == "d":
        decrypt_file(file_path, password)
    else:
        print("Invalid option. Please enter 'e' or 'd'.")


if __name__ == "__main__":
    main()
