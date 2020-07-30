def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 101, 10):
        print(i, end=' ')
    print()

    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

    amountofstars = int(input("Please enter the amount of stars: "))
    for i in range(amountofstars):
        print('*', end=' ')

    for i in range(0, amountofstars + 1):
        print('*' * i)

main()