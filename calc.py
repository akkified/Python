def calc(num1,num2,operation):
    if operation == "Add":
        print(num1 + num2)
    elif operation == "Subtract":
        print(num1 - num2)
    elif operation == "Multiply":
        print(num1 * num2)
    elif operation == "Divide":
        print(num1/num2)
    else:
        print("You entered the wrong operation you moron!")

calc(1,3,Add)

