#username validation 

name = input("Enter your name: ")

if " " in name:
    print("Please provide a valid name without spaces.")
elif len(name) > 12:
    print("Please provide a name with less than 12 characters.")
elif not name.isalpha():
    print("Please provide a name that does not contain numbers.")
else:
    print(f"Hello, {name}.")

    
