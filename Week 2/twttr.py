


# def main():
#     text = input("Input: ")
#     vowels = "aeiouAEIOU"
#     result = "".join(char for char in text if char not in vowels)
#     print(f"Output: {result}")


# main()




def main():
    text = input("Input: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for i in text:
        if i not in vowels:
            result += i
    print("Output:", result)

main()