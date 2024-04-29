def askInt():
    # Ask for how many numbers to save
    n = int(input("Enter a positive integer: "))

    # List to store the numbers
    numbers = []

    # Ask users for numbers to save until list is full and save it to the list
    for n in range(n):
        x = int(input("Enter a number: "))
        numbers.append(x)

    for x in numbers:
        print(x)

    # Ask for the  number to look for in the list
    key = int(input("Enter a number to search: "))

    # If the key is not found, index is set to -2
    index = numbers.index(key) if key in numbers else -2
    
    # Add 1 to the index because we want it to start from 1 to N
    print(index+1)

def main():
   askInt()

if __name__ == "__main__":
    main()