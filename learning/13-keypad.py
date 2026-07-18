keypad = [
["1", "2", "3"],
["4", "5", "6"],
["7", "8", "9"],
["*", "0", "#"]
]

for row in keypad:
    for button in row:
        print(button, end=" ")
    print()