products = ["milk","bread","eggs","apple"]
basket = []
print("Items available: ")
for product in products:
    print(product)
while True:
    choice = input("What do you want?(type 'quit' to exit): ").lower()
    if choice == 'quit' :
        print("Exiting the program, thank you!")
        break
    if choice in products:
        basket.append(choice)
        print(f"Added {choice} to your basket. ")

        print("You now have: ")
        for items in basket:
            print(f"-{items}")
    else:
        print(f"We do not have {choice}, please choose another product. ")


    



