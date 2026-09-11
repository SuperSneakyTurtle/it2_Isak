valid_num: bool = False

while valid_num != True:
    num = input("Type a number:")
    try:
        num = int(num)
        valid_num = True
    except ValueError:
        print("Type a number you idiot.")

print(f"You typed the number {num}")