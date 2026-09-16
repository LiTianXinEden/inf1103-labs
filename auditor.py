inventory = 0
while inventory < 5:
    stock = input("Enter stock ")
    if stock == "quit":
        break
    elif stock.isdigit() == False:
        print("Error: not accepted input, try again")
        continue
    inventory = inventory + int(stock)
    print(inventory)
if inventory < 5:
    print("ended")
else:
    print("inventory more than 5")
