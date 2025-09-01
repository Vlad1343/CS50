
import re
import sys

def main():
    ip_address = input("IPv4 Address: ")
    print(validate(ip_address))

def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)
    if not match:
        return False
    parts = match.groups()
    for part in parts:
        try:
            num = int(part)
            if not (0 <= num <= 255):
                return False
        except ValueError:
             return False

    return True


if __name__ == "__main__":
    main()
