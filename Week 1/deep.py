answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()
normalized = answer.lower()
if normalized == "42" or normalized == "forty-two" or normalized == "forty two":
    print("Yes")
else:
    print("No")
