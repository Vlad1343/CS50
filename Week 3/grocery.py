def main():
    grocery = {}
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            print()
            break
        if item:
            grocery[item] = grocery.get(item, 0) + 1
    for item in sorted(grocery):
        print(grocery[item], item)


main()
