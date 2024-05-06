def menu():
    # Ask for how many numbers to save
    n = int(input("Enter a positive integer: "))

    # List to store the numbers
    numbers = []

    # Ask users for numbers to save until list is full and save it to the list
    for n in range(n):
        x = int(input("Enter a number: "))
        numbers.append(x)

    return numbers