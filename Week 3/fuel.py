while True:
    try:
        fraction = input("Fraction: ")
        parts = fraction.split("/")
        x = int(parts[0])
        y = int(parts[1])
        if y == 0 or x > y:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        print("Invalid value")
    else:
        break

maths = round(x/y * 100)
if maths >= 99:
    print("F")
elif maths <= 1:
    print("E")
else:
    print(f"{maths}%")
