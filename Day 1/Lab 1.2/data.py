# This script demonstrates the use of list, dict and class
# as data structure

class Staff:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_retire(self):
        if self.age >= 60:
            print(f"{self.name} can retire.")
        else:
            print(f"{self.name} still need to work.")


def main():

    # Example of using list
    # Create a list of number
    number_list = [2, 3, 5, 7, 11]

    # Loop and print all element in list
    for number in number_list:
        print(number)
    print()


    # Example of using dictionary
    # Create a dict of plate number and car owner
    cars = {
        "VDP 1008": "Mr. Halim",
        "DX 67": "Ir. Azhar",
        "PAU 123": "Dr. Kelly",
    }

    # Assign new key-value pair
    cars["TG 819"] = "Ms. Devi"

    # Loop and print key-values
    for car, owner in cars.items():
        print(f"{car} owner is {owner}.")
    print()


    # Example of using Class

    # Create a staff instances
    staff1 = Staff("Prof. Ayyub", 60)
    staff2 = Staff("Dr. Wan", 40)

    print(f"{staff1.name} is {staff1.age} years old.")
    staff1.check_retire()

    print(f"{staff2.name} is {staff2.age} years old.")
    staff2.check_retire()

    return

if __name__ == "__main__":
    main()
