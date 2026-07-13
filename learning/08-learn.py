#interest calculator

principle = float(input("Enter the principle amount: "))
if principle <= 0:
    print("Principle amount must be greater than 0.")
    principle = float(input("Enter the principle amount: "))

rate = float(input("Enter the interest rate: "))
if rate <= 0:
    print("Interest rate must be greater than 0.")
    rate = float(input("Enter the interest rate: "))

time = int(input("Enter the time period: "))
if time <= 0:
    print("Time period must be greater than 0.")
    time = int(input("Enter the time period: "))

total = principle * pow(1 + (rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")

