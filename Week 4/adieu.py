import inflect

def main():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    if names:
        names_str = p.join(names)
        print(f"Adieu, adieu, to {names_str}")


main()
