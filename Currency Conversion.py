choices = input("Type 1 to convert from £ to $, or type 2 to convert from $ to £")
exchange_rate = float(input("Enter the exchange rate: "))
if choices == "1":
    amount = float(input("Enter your amount in pounds: "))
    total = amount * exchange_rate
    print(f"${amount:.2f} in dollars is: {total:.2f}")
else:
    amount = float(input("Enter your amount in dollars: "))
    total = amount / exchange_rate
    print(f"${amount:.2f} in pounds is: {total:.2f}")
