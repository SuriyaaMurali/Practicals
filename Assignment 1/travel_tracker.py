menu = "\nmenu:\n(L) - list required places\n(A) - add new place\n(M) - mark a place as visited\n(Q) - quit"


# noinspection PyStringFormat
def main():
    #   Opens and reads places.csv file
    places_file = open('places.csv', 'w+')
    places_data = places_file.readlines()
    places_details = []
    visited_places_details = []
    # Filter data from file into two list
    for places_line in places_data:
        if "r" in places_line:
            places = places_line.strip().split(",")
            places_details.append(places)
        else:
            places = places_line.strip().split(",")
            visited_places_details.append(places)
    print(places_details)
    # welcome message and menu
    print('Travel Tracker 1.0 - by Suriyaa Murali')
    print('3 places loaded from places.csv')
    print(menu)

    choice = input('>>> ').upper()
    while choice != "Q":
        # Shows main menu to user
        if choice == "L" or choice == "l" or choice == "1":
            for places_file in places_details:
                print('{} {:,.2f} {}\n'.format(places_details))
            choice = input('>>> ').upper()
        # shows visited places to users or returns error message if there are none
        elif choice == "M":
            if visited_places_details != "":
                for _ in visited_places_details:
                    print('{} ${:,.2f} ({})'.format(visited_places_details, visited_places_details,
                                                    visited_places_details))
                choice = input('>>> ').upper()
            else:
                print("No visited places")
                choice = input('>>> ').upper()
        # ask user for item details and append them to require item list
        elif choice == "A" or choice == "a" or choice == "2":
            added_place_details = []
            place_name = input("Name:")
            if place_name == "":
                print('input name cannot be empty')
            place_country = input("Country:")
            if place_country == "":
                print('input cannot be empty')
            if place_name == "":
                print('input cannot be empty')
            added_place_details.append(place_name)
            places_details.append(added_place_details)
            print(places_details)

            choice = input('>>> ').upper()
            # show require items that can be mark as visited and total number items.
        elif choice == "M" or choice == "m" or choice == "3":
            for _ in places_details:
                print(places_details)
            number_of_places = len(places_details)
            total_price_of_places = sum(places_details)
            print("Total Number of places {} and Priority {}".format(number_of_places, total_price_of_places))
            choice = input('>>> ').upper()
        # Exits program
        elif choice == "Q" or choice == "q" or choice == "4":
            print("goodbye")
            places_data.append(places_details)
            places_data.append(places_details)
            places_file.write(places_data)
            places_file.close()
        # error check for choice
        else:
            print('Invalid choice')
            print(menu)
            choice = input('>>> ').upper()


main()
