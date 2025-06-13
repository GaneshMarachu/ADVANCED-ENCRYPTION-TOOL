import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

# Constants
BUFFER_SIZE = 65536  # 64KB
KEY_SIZE = 32  # For AES-256
SALT_SIZE = 16
IV_SIZE = 16
PASSWORD = input("Enter password for encryption/decryption: ").encode()

def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=1000000)

def encrypt_file(input_path, output_path):
    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(PASSWORD, salt)
    iv = get_random_bytes(IV_SIZE)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)

    with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        f_out.write(salt + iv)  # Save salt and IV at start
        while chunk := f_in.read(BUFFER_SIZE):
            f_out.write(cipher.encrypt(chunk))
    print(f"[✓] File encrypted: {output_path}")

def decrypt_file(input_path, output_path):
    with open(input_path, 'rb') as f_in:
        salt = f_in.read(SALT_SIZE)
        iv = f_in.read(IV_SIZE)
        key = derive_key(PASSWORD, salt)
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)

        with open(output_path, 'wb') as f_out:
            while chunk := f_in.read(BUFFER_SIZE):
                f_out.write(cipher.decrypt(chunk))
    print(f"[✓] File decrypted: {output_path}")

def main():
    print("===== AES-256 File Encryption Tool =====")
    choice = input("Choose: [1] Encrypt  [2] Decrypt: ")

    if choice == '1':
        input_path = input("Enter path to file to encrypt: ")
        output_path = input("Enter path to save encrypted file: ")
        encrypt_file(input_path, output_path)
    elif choice == '2':
        input_path = input("Enter path to encrypted file: ")
        output_path = input("Enter path to save decrypted file: ")
        decrypt_file(input_path, output_path)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
