import re
import sys
import quopri
import hashlib
import ipaddress
import requests
import email

def read_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    parser = email.parser.BytesParser()
    msg = parser.parsebytes(content)
    return msg

def main(file_path):
    email_message = read_file(file_path)
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)