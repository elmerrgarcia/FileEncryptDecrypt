# 🔐 Python File Encryptor/Decryptor

A sleek, terminal-based file security tool built with Python. This utility uses **AES-128 (Fernet)** symmetric encryption to secure any file type, including PDFs, images, and text documents.

!

## ✨ Features
* **ASCII Art Interface:** Powered by `pyfiglet`.
* **Symmetric Encryption:** High-security file scrambling.
* **Safety First:** Automatically handles binary data to prevent file corruption.
* **Extension Management:** Adds `.locked` to encrypted files to keep your originals safe.

## 🚀 Getting Started

### Prerequisites
You will need Python 3.x installed. Install the required libraries using pip:

```bash
pip install cryptography pyfiglet
Installation
Clone the repository:

Bash
git clone [https://github.com/elmerrgarcia/FileEncryptDecrypt.git](https://github.com/elmerrgarcia/FileEncryptDecrypt.git)
Navigate to the folder:

Bash
cd "File Encryption"
🛠️ How to Use
Generate a Key: Run the script and select Option 3. This creates a secret.key file.

Encrypt: Select Option 1 and enter the filename (e.g., my_data.pdf).

Decrypt: Select Option 2 and enter the filename (e.g., my_data.pdf.locked).

[!CAUTION] DO NOT LOSE YOUR secret.key FILE. If you lose the key, or if you generate a new one over the old one, any files encrypted with the previous key will be permanently unrecoverable.

🛡️ Security Note
The .gitignore file is configured to ignore secret.key. Never upload your key to a public repository. If you share an encrypted file with someone, you must provide them with the key via a separate, secure channel.

📜 License
This project is open-source and available under the MIT License.
