
# File Encryptor

This Python application provides an encryption and decryption solution for files in a specified directory. Built using the `cryptography` library and `tkinter` for a user-friendly GUI, it securely encrypts files with a key file contained in a password-protected `.7z` archive.

## Features

- **Automated File Encryption**: Encrypts files in the current directory automatically upon startup.
- **Automated Decryption Process**: After encryption, the program prompts for a secret phrase to decrypt the files.
- **Password-Protected Key File**: The encryption key is stored in a `.7z` archive that is password-protected, enhancing security.
- **GUI**: Simple, intuitive interface using `tkinter` for user interaction and output display.

## How It Works

1. **Decryption of Key**: The program starts by decrypting the `.7z` file containing the key, using a hardcoded password.
2. **File Encryption**: After extracting the key, it proceeds to encrypt all files in the directory except excluded files.
3. **File Decryption**: Users are prompted to enter a secret phrase. Upon correct entry, the program decrypts the encrypted files.

## Prerequisites

Ensure you have the following libraries installed:

```bash
pip install cryptography py7zr
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/file-encryptor.git
cd file-encryptor
```

## Usage

1. **Run the Program**: Launch the program by running the `samael.py` file:

   ```bash
   python samael.py
   ```

2. **Encryption Process**: Upon launching, the program automatically encrypts files in the directory.

3. **Decryption Process**: After encryption, the program will prompt you for the secret phrase to decrypt files.

## File Structure

- `samael.py`: Main script with the encryption and decryption logic.
- `protected_key.7z`: Password-protected archive containing the encryption key.
- `thekey.key`: Encryption key (automatically extracted by the program).

## Configuration

The hardcoded password for `.7z` decryption is set to `01123581321`, and the decryption secret phrase is `Joydeep2005!`. You can modify these values in `samael.py`.

## Security Note

Keep the `.7z` password and the decryption phrase secure to ensure file protection. **Avoid using this in a production environment without enhancing security measures**.

---

## Contributing

Feel free to submit pull requests for new features, bug fixes, or any improvements to the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This README covers setup, usage, and key details of the project.
