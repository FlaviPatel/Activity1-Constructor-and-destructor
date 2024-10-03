class Employee:
    # Constructor
    def __init__(self):
        print("Employee Created!")

    # Destructor
    def __del__(self):
        print("Employee deleted !")

# Main
# Created the object
employee1 = Employee()
del employee1
