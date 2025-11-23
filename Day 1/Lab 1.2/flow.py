# This script demonstrate how to control flow using
# if-clause, for-loop and while-loop
import random

def main():

    # Generate random number
    a = random.randint(1, 10)

    # Using if clause to control flow
    if a < 5:
        print("a is smaller than 5")
    elif a < 8:
        print("a is between 5 and 7 inclusive")
    else:
        print("a is between 8 and 10 inclusive")

    print(f"a is {a}")
    print()


    # For loop starting from 0 to 9
    for i in range(10):
        print("This is round", i)
    print()


    b = 0
    # While loop
    while b != 7:
        b = random.randint(1, 6) 
        if b == 3:
            print(f"b is 3. break.")
            break
        print(f"b is {b}. keep looping.")
    print()

    return

if __name__ == "__main__":
    main()
