while True:

    def add(a, b):
        return a + b


    def subtract(a, b):
        return a - b


    def multiply(a, b):
        return a * b


    def divide(a, b):
        return a / b


    print("my magical calculator")

    print("Select an operation")

    print("1.Add \n 2.subtract \n 3.Multiply \n 4.Divide \n")

    choice =int(input("Enter Your Choice of Operation..\n 1 or 2 or 3 or 4"))

    num = float(input("Please enter your first number"))
    num2 = float(input("please enter your second number"))

    if choice == 1:
        print(add(num, num2))
    elif choice == 2:
        print(subtract(num, num2))
    elif choice == 3:
        print(Multiply(num, num2))
    elif choice == 4:
        print(divide(num, num2))
    else:
        exit("invalid code")
