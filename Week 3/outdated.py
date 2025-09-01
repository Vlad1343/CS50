months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if "/" in date:
        try:
            parts = date.split("/")
            if len(parts) != 3:
                raise ValueError
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
        except ValueError:
            continue
    elif "," in date:
        try:
            parts = date.split()
            if len(parts) != 3:
                raise ValueError
            month_name = parts[0].title()
            if month_name not in months:
                raise ValueError
            day = int(parts[1].replace(",", ""))
            year = int(parts[2])
            month = months.index(month_name) + 1
        except ValueError:
            continue
    else:
        continue

    if 1 <= month <= 12 and 1 <= day <= 31:
        print(f"{year:04}-{month:02}-{day:02}")
        break
