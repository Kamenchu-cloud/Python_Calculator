def user_specifications():
    # Assign variables to the user's specific inputs
    user_input1 = float(input("Enter first value: "))  # Convert to float
    user_input2 = float(input("Enter second value: "))  # Convert to float
    user_option = input("Select action (Addition, Subtraction, Multiplication, Division): ")

    # Assign variables to their corresponding values and store them in a dictionary
    variables = {"num_1": user_input1, "num_2": user_input2, "option": user_option}

    return variables

def compute_addition(num_1, num_2):
    result = num_1 + num_2
    print(f"{num_1} added to {num_2} is {result}")
    return result

def compute_subtraction(num_1, num_2):
    result = num_1 - num_2
    print(f"{num_2} subtracted from {num_1} is {result}")
    return result

def compute_multiplication(num_1, num_2):
    result = num_1 * num_2
    print(f"{num_1} multiplied by {num_2} is {result}")
    return result

def compute_division(num_1, num_2):
    if num_2 == 0:
        print("Cannot divide by zero")
        return None
    else:
        result = num_1 / num_2
        print(f"{num_1} divided by {num_2} is {result}")
        return result

def compute(num_1, num_2, option):
    if option == "Addition":
        return compute_addition(num_1, num_2)
    elif option == "Subtraction":
        return compute_subtraction(num_1, num_2)
    elif option == "Multiplication":
        return compute_multiplication(num_1, num_2)
    elif option == "Division":
        return compute_division(num_1, num_2)

if __name__ == '__main__':
    variables = user_specifications()
    result = compute(num_1=variables["num_1"], num_2=variables["num_2"], option=variables["option"])
    if result is not None:
        print("Result:", result)
