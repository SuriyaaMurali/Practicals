def main():
    finished = False
    result = 0
    while not finished:
        try:
            result = int(input("Enter a number: "))
            print (result)
        except ValueError:
            print("Enter a valid number!")

        print("Valid result is:", result)


main()
