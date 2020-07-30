def main():
    import random

    MAX_INCREASE = 0.175  # 17.5%
    MAX_DECREASE = 0.05  # 5%
    MIN_PRICE = 1.0
    MAX_PRICE = 100.0
    INITIAL_PRICE = 10.0
    OUTPUT_File = ''


    out_file = open("../../../AppData/Roaming/JetBrains/PyCharm2020.1/scratches/OUTPUT_FILE.txt", 'w')
    day_counter = 0
    price = INITIAL_PRICE
    print("${:,.2f}".format(price))

    while price >= MIN_PRICE and price <= MAX_PRICE:
        price_change = 0
        day_counter += 1

        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)

        else:

            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print("On day {} price is: ${:,.2f}".format(day_counter, price), file=out_file)
    out_file.close()
main()
