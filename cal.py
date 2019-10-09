import math
print("Hello everybody")
while True:
    print("\nChoose the math operation.\n\n0 - Additional\n1 - Subtraction\n2 - Multiplication\n3 - Division"
          "\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n"
          "10 - Tangent")
    oper = input("\nYour option from the menu: ")

    # Addition
    if oper == '0':
        first_value = float(input("Enter the first value: "))
        second_value = float(input("Enter the second value: "))

        print("\nThe result is: " + str(first_value + second_value) + "\n")

        # Going back to the main menu
        back = input("\nDo you want to go back to main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    # Subtraction
    elif oper == '1':
        first_value = float(input("Enter the firs value: "))
        second_value = float(input("Enter the second value: "))

        print("\nThe result is: " + str(first_value - second_value) + "\n")

        # Going back to the main menu
        back = input("\nDo you want to go back to the main menu? (y/n) ")
        if back == 'y':
            continue
        else:
            break

    # Multiplication
    elif oper == '2':
        first_value = float(input("Enter the first value: "))
        second_value = float(input("Enter the second value: "))

        print("The result is: " + str(first_value * second_value) + "\n")

        # Going back to the main menu
        back = input("Do you want to back to the main menu? (y/n) ")
        if back == 'y':
            continue
        else:
            break

    # Division
    elif oper == '3':
        first_value = float(input("Enter the first value: "))
        second_value = float(input("Enter the second value: "))

        print("The result is : " + str(first_value / second_value) + "\n")

        # Going back to the main menu
        back = input("Do you want to go back to the main menu? (y/n) ")
        if back == 'y':
            continue
        else:
            break

    # Modulo
    elif oper == '4':
        first_value = float(input("Enter the first value: "))
        second_value = float(input("Enter the second value: "))

        print("The result is: " + str(first_value % second_value) + "\n")

        # Going back to the main menu
        back = input("Do you want to go back to the main menu? (y/n)")
        if back == 'y':
            continue
        else:
            break

    # Power
    elif oper == '5':
        first_value = float(input("Enter the first value: "))
        second_value = float(input("Enter the second value: "))

        print("The result is: " + str(math.pow(first_value, second_value)) + "\n")

        # Going back to the main menu
        back = input("Do you want to go back to the main menu? (y/n) ")
        if back == 'y':
            continue
        else:
            break

    # Square root
    elif oper == '6':
        value = float(input("Enter the value: "))

        print("The result is: " + str(math.sqrt(value)) + "\n")

        # Going back to the main menu
        back = input("Do you want to go back to the menu? (y/n)")
        if back == 'y':
            continue
        else:
            break

    # Logarithm
    elif oper == '7':
        value = float(input("Enter a value: "))

        print("The result is: " + str(math.log(value, 2)) + "\n")

        # Going back to the main menu
        back = input("Do you want to go back to the main menu? (y/no) ")
        if back == 'y':
            continue
        else:
            break

    # Sine
    elif oper == '8':
        value = float(input("Enter a value: "))

        print("The result is: " + str(math.sin(math.radians(value))) + "\n")

        # Going back to the main menu
        back = input("Do you want to go back to the main menu? (y/n)")
        if back == 'y':
            continue
        else:
            break

    # Cosine
    elif oper == '9':
        value = float("Enter a value: ")

        print("The result is:" + str(math.cos(value)) + "\n")

        # Going back to the main menu
        back = input("Do you want to go back to the main menu? (y/n)")
        if back == 'y':
            continue
        else:
            break

    # Tangent
    elif oper == '10':
        value = float(input("Enter a value: "))

        print("The result is: " + str(math.tan(value)) + "\n")

        # Going back to the main menu
        back = input("DO you want to go back to the main menu? (y/n) ")
        if back == 'y':
            continue
        else:
            break

    # Handling invalid options
    else:
        print("\nInvalid option!\n")
        continue
