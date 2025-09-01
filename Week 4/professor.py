import random

def main():
    level = get_level()
    score = 0
    used_pairs = []



    for _ in range(10):
        while True:
            x = generate_integer(level)
            y = generate_integer(level)
            pair = (x, y)
            if pair not in used_pairs:
                used_pairs.append(pair)
                break

        correct_answer = x + y
        attempts = 3



        while attempts > 0:
            user_input = input(f"{x} + {y} = ")
            try:
                user_answer = int(user_input)
            except ValueError:
                print("EEE")
                attempts -= 1
                continue


            if user_answer == correct_answer:
                score += 1
                break
            else:
                print("EEE")
                attempts -= 1
        else:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")



def get_level():
    while True:
        level = input("Level: ")
        if level in {'1', '2', '3'}:
            return int(level)


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError



if __name__ == "__main__":
    main()
