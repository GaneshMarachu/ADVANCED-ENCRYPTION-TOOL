COMPANY: CODTECH IT SOLUTIONS

NAME: Marachu Ganesh

INTERN ID:CT06DL1340

DOMAIN: SQL

DURATION: 6 WEEEKS

MENTOR: NEELA SANTOSH

# ADVANCED-ENCRYPTION-TOOL

This project presents a command-line based encryption and decryption tool built with Python, utilizing the Advanced Encryption Standard (AES) with 256-bit encryption. Designed as part of a cybersecurity internship task, the purpose of this tool is to offer a secure, user-friendly method for protecting sensitive files by encrypting them before storage or transmission, and then decrypting them when needed.

The tool uses the `cryptography` library, one of the most secure and widely used Python packages for implementing modern cryptographic techniques. AES-256 is a symmetric encryption algorithm, meaning the same password is used for both encryption and decryption. The implementation follows best practices such as deriving keys from user-provided passwords using a secure Key Derivation Function (KDF), and it includes random salt and initialization vector (IV) generation to ensure each encryption operation is unique and secure, even with the same password.

The interface is kept simple for learning and demonstration purposes. When the user runs the script, they are prompted to enter a password, which is internally converted into a strong encryption key using PBKDF2HMAC. The script then asks whether the user wants to encrypt or decrypt a file. Depending on the selection, the user provides the path to the input file and the destination path for the output file. If encryption is chosen, the tool will securely encrypt the content of the file and save the output. If decryption is chosen, it will verify the key against the encrypted data and safely return the original file contents.

This project is not only a demonstration of how AES-256 works but also a good example of practical cybersecurity application. Encryption is one of the fundamental concepts in information security, and this task provides hands-on experience with how encryption can be used to protect data confidentiality. Real-world applications of such a tool include securing local files, email attachments, backups, or any sensitive documents.

The implementation also includes error handling for common mistakes such as incorrect file paths, permission errors, or password mismatches during decryption. This helps the user understand typical pitfalls in secure data handling. To use this tool effectively, the user should provide valid file paths and remember the password used during encryption, as the data cannot be recovered without the correct key.

The tool is kept modular and simple on purpose, making it easier to extend with features like a GUI, drag-and-drop interface, or even integration with cloud storage encryption. The current implementation is ideal for learning, experimenting, and getting comfortable with real-world cryptographic workflows.

In summary, this encryption-decryption tool is a robust, secure, and easy-to-use Python application that highlights the strength and importance of AES-256 in cybersecurity. It aligns well with the goal of demonstrating real-world security mechanisms and provides a solid foundation for further exploration in file security and cryptographic programming.
