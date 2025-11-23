# This script demonstrate how to use Python function
import math

def greet(name):
    return f"Hello {name}"


def double_sin(theta):
    return 2.0 * math.sin(theta)


def main():

    print(greet("Ali"))
    print(double_sin(math.pi/4))

    return

if __name__ == "__main__":
    main()
