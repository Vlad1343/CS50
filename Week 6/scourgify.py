

import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            data = []
            for row in reader:
                name = row['name']
                house = row['house']
                last, first = name.split(', ')
                data.append({'first': first, 'last': last, 'house': house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    try:
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        sys.exit(f"Error writing to {output_file}: {e}")

if __name__ == "__main__":
    main()
