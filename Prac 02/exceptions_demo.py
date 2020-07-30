def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        #adding a while loop to the program to avoid ZeroDivisionError.
        while denominator == 0:
            denominator = int(input("Denominator cannot be 0, try again: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")

    print("Finished.")
main()

# 1. When will a ValueError occur?
#   ValueError occurs when the user inputs something else other than a number.

# 2. When will a ZeroDivisionError occur?
#   ZeroDivisionError occurs when the denominator is zero.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#   We can make the program loop until the user inputs a denominator that is not zero.