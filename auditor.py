inventory = 0
failedEntries = 0
while inventory < 500:
    stock = input("Enter stock ")
    if stock == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", failedEntries)
        break
    elif stock.isdigit() == False: #this for rejecting invalid input like ten or negative num
        failedEntries = failedEntries + 1
        print("Error: not an accepted input, try again") 
        continue
    inventory = inventory + int(stock)
    print("Total Inventory:", inventory)
if inventory > 500:
    print("Inventory more than 500")
