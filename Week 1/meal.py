def main():
    time = input("What time is it? ")
    convert(time)
    if 7 <=convert(time)<= 8:
        print("breakfast time")
    elif 12 <=convert(time)<= 13:
        print("lunch time")
    elif 18 <=convert(time)<= 19:
        print("dinner time")
    else:
        pass



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = hours + minutes / 60
    return time


if __name__ == "__main__":
    main()
