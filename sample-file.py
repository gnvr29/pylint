# This is a module comment
# It's a bit too long and not very descriptive

import os, sys # Multiple imports on one line

GLOBAL_VARIABLE = "I am a global variable" # Global variable, often discouraged 

class MyClass:
    """
    This is a class that does something.
    Maybe it does nothing, who knows?
    It has a very short docstring.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.data_list = []
        self.public_member = "hello" # Public member for demonstration

    def calculate_something(self, a, b):
        """
        Calculates something.
        """
        result = a + b # Simple calculation
        another_result = result * 2
        print("Calculation done.") # Print statement inside method
        if another_result > 10:
            return another_result # Inconsistent return
        else:
            return # Missing return value

    def _private_method(self):
        """A private method."""
        print("This is a private method.")
        pass # Using pass unnecessarily

    def process_data(self, input_data):
        """
        Processes some input data.
        Does not validate input_data type.
        """
        for item in input_data: # Looping over input_data without checking if it's iterable
            self.data_list.append(item.upper()) # Assumes item has .upper() method

    def duplicate_method(self, x, y):
        z = x + y
        return z

    def duplicate_method(self, a, b): # Duplicate method definition (overwrites the first one)
        c = a * b
        return c

def stand_alone_function(param1, param2):
    """
    This is a standalone function.
    It has too many arguments and too many local variables.
    """
    local_var1 = param1 * 2
    local_var2 = param2 / 2
    temp_result = local_var1 + local_var2
    if temp_result > 50:
        print("Result is large!")
        return True
    else:
        print("Result is small.")
        return False

def another_function(arg1, arg2):
    """Another function."""
    if arg1 > arg2:
        return arg1
    else:
        return arg2
    return "This return is unreachable." # Unreachable code

class AnotherClass:
    def __init__(self):
        self.some_value = 0

    def get_value(self):
        return self.some_value

    def set_value(self, value):
        self.some_value = value

    def perform_action(self):
        a = 5
        b = 10
        c = a + b
        if c > 100: # Magic number
            print("C is very large.")
        else:
            print("C is not that large.")
        # Variable 'd' defined but not used
        d = c * 2


def unused_import_function():
    """Function to demonstrate unused import."""
    # os is imported but not used here
    # sys is imported but not used here
    pass

if __name__ == "__main__":
    my_obj = MyClass("Alice", 30)
    print(my_obj.calculate_something(5, 7))
    my_obj._private_method() # Accessing "private" method directly

    data_to_process = ["apple", "banana", 123] # One item is not a string
    my_obj.process_data(data_to_process)
    print(my_obj.data_list)

    result_func = stand_alone_function(100, 200)
    print(result_func)

    an_obj = AnotherClass()
    an_obj.set_value(25)
    print(an_obj.get_value())
    an_obj.perform_action()

    # Accessing global variable directly
    print(GLOBAL_VARIABLE)

    # Some complex expression with bad spacing
    x=10
    y=20
    z = x + y*2 - 5 / 2

    # Unused variable
    unused_var = "I am not used"

    # Redundant parentheses
    if (True):
        print("Always true.")

    # Multiple statements on one line
    a = 1; b = 2; print(a+b)

    #line that's way too loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong

    # Empty block
    for i in range(5):
        if i == 3:
            # TODO: Implement something here later
            pass