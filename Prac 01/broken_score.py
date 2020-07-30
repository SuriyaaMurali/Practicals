def main():
    score = float(input("Enter score: "))
    while not 0 <= score <= 100:
        score = (float(input("Score must be between 0 and 100. Please try again: ")))

    if score >= 90:
        print("Excellent")
    elif score >= 50 < 90:
        print("Passable")
    else:
        print("Bad")

main()

