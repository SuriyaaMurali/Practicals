
MENU_PROMPT = "q)uit, c)hoose taxi, d)rive"

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def list_taxis():
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def menu():
    current_bill = 0
    print(MENU_PROMPT)
    menu_choice = input(">>> ").lower()

    while menu_choice != 'q':
        if menu_choice == 'c':
            print("Taxis available:")
            list_taxis()
            taxi_choice = int(input("Choose taxi: "))
            print("Bill to date: ${:.2f}".format(current_bill))

        elif menu_choice == 'd':
            drive_distance = int(input("Drive how far? "))
            taxis[taxi_choice].drive(drive_distance)
            print("Your {} trip cost you ${:.2f}".format(taxis[taxi_choice].name, taxis[taxi_choice].get_fare()))
            current_bill += taxis[taxi_choice].get_fare()
            print("Bill to date: ${:.2f}".format(current_bill))

        else:
            print("Invalid menu choice")

        print(MENU_PROMPT)
        menu_choice = input(">>> ").lower()


def main():
    print("Let's drive!")
    menu()
    print("Taxis are now:")
    list_taxis()


if __name__ == '__main__':
    main()
