def even_numbers():
    try:
        n = int(input("Enter the integer"))
    except Exception as e:
        print("User input is not an integer")
    else:
        if n%2 == 0:
            print(n," is even number")
        else:
            print(n, " is not an even number")