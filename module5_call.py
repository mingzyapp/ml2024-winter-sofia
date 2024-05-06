def search(num):
    
    key = int(input("Enter a number to search: "))

    # If the key is not found, index is set to -2
    index = num.index(key) if key in num else -2
    
    # Add 1 to the index because we want it to start from 1 to N
    print(index+1)