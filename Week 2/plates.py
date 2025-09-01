
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Length must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: First two characters must be letters
    if not s[:2].isalpha():
        return False

    # Rule 3: No special characters or spaces
    if not s.isalnum():
        return False

    # Rule 4 & 5: Numbers must be at the end, and the first number cannot be '0'
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                # First digit check (no leading zeros)
                if char == "0":
                    return False
                number_started = True
            elif not s[i:].isdigit():  # If numbers are not at the end
                return False

    return True  # If all checks pass, the plate is valid

main()