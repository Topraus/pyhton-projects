menu = {"popcorn": 4.50,
        "cola": 1.50,
        "fries": 2.00,
        "nachos": 3.60,
        "soda": 2.00,
        "lemonade": 2.20,
        "chips": 3.00,}
print("------- MENU -------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("--------------------")

cart = []
total = 0

while True:

    choice = input("What would you like to get?(q to quit): ").lower()
    if choice == "q":
        break
    if choice in menu:
        print(f"{choice} added to your cart.")
        cart.append(choice)
        total += menu[choice]
    else:
        print("We do not have that, sorry.")

print("------ ITEMS ------")

for item in cart:
    print(item)

print("-------------------")

print(f"Total price is ${total:.2f}.")




                        