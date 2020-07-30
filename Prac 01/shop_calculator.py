def main():
    total = 0
    itemprice = []
    items = 1
    amountofitems = int(input("Please enter the amount of items for checkout: "))
    while amountofitems < 0:
        amountofitems = int(input("Number of items must be greater then 0.\ Please try again: "))

    for i in range(1, amountofitems + 1):
        itemprices = float(input("Please enter price of item {}: ".format(i)))
        itemprice.append(itemprices)
        total =(total + itemprices)

    for i in itemprice:
        print("Price for item {}: ${}",(items, itemprice, [items - 1]))
        items += 1
    if total > 100:
        total = total - (total * 0.10)
    else:
        pass

    print("Total price for", (items), "items is $",(total))

main()
