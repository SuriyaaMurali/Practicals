def main():
    output_file = open("name.txt", 'w')
    user_name = input("Please enter your name: ")
    print(user_name, file=output_file)
    output_file.close()

    in_file = open("name.txt", 'r')
    name = in_file.readline().strip()
    print("Your name is {}".format(name))
    in_file.close()

    in_file = open("numbers", 'r')
    number_one = int(in_file.readline().strip())
    number_two = int(in_file.readline().strip())
    sum_of_numbers = number_one + number_two
    print(sum_of_numbers)
    in_file.close()

    in_file = open("Infinite_numbers.txt", 'r')
    sum_numbers = 0
    for i in in_file:
        number = int(i)
        sum_numbers += number
    print(sum_numbers)
    in_file.close()

main()