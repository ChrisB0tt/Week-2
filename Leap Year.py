year = int(input("Enter the year you were born: "))
if year % 4 == 0:
    print("You were born in a leap year")
else:
    print("You were not born in a leap year")


if year < 2006:
    print("You are older than me.")
elif year > 2006:
    print("You're younger than me.")
elif year == 2006:
    print("You're the same age as me.")
