row = int(input("Please enter the number of rows: "))   
symbol = input("Please enter the symbol you want to use: ")

for i in range(row, 0, -1):
    for j in range(i):
        print(symbol, end="")
    print()