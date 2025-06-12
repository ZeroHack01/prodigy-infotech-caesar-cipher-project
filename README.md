Caesar Cipher Project
Overview

The Caesar Cipher Project is a Python-based implementation of the Caesar Cipher encryption and decryption algorithm. The Caesar Cipher is one of the simplest and oldest methods of encryption, named after Julius Caesar, who used it to securely communicate with his generals. This project demonstrates the basic principles of encryption and decryption using this classical technique.
Purpose

This project was developed as part of an internship program at Prodigy Infotech.

    Encryption: Convert plaintext to ciphertext using a specified shift value.
    Decryption: Convert ciphertext back to plaintext using the same shift value.
    Command-Line Interface (CLI): Easy to use directly from the terminal or command line.

Installation

To get started with this project, you have a couple of options:

    Clone the Repository:

    Clone the repository to your local machine using Git:

    bash

    git clone https://github.com/yourusername/prodigy-infotech-caesar-cipher-project.git

    Replace yourusername with your GitHub username.

    Download the Script:

    Alternatively, you can manually download the prodigy_infotech_caesar_cipher.py file from the repository.

Usage

    Navigate to the Project Directory:

    Change your working directory to where the prodigy_infotech_caesar_cipher.py script is located:

    bash

cd path/to/your/project

Run the Script:

To encrypt a message:

bash

python3 prodigy_infotech_caesar_cipher.py "Your Message" <shift> encrypt

To decrypt a message:

bash

    python3 prodigy_infotech_caesar_cipher.py "Your Message" <shift> decrypt

    Replace "Your Message" with the text you want to encrypt or decrypt and <shift> with the integer value representing the number of positions to shift in the alphabet.

Example

Encrypting a message:

bash

python3 prodigy_infotech_caesar_cipher.py "Hello World" 3 encrypt

Output:

Khoor Zruog

Decrypting a message:

bash

python3 prodigy_infotech_caesar_cipher.py "Khoor Zruog" 3 decrypt

Output:

Hello World

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions to this project are welcome. Please follow the guidelines provided in the repository for submitting issues and pull requests.