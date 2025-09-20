def is_even(n):

    """
    This function returns whether a number is even
    Provide the input as an valid interger

    """
    if type(n) == int:
        if n%2 == 0:
            print(f"the number {n} is even")
        else:
            print(f"the number {n} is odd")
    else:
        print("invalid input")
x = input("Enter the number to check whether it is even or odd")
is_even(x)
        