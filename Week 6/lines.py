

import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                stripped = line.lstrip()
                if not stripped:
                    continue
                if stripped.startswith('#'):
                    continue
                count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
