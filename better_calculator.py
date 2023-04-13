# Calculator to perform basic arithmetic operations
valid_nums = [0,1,2,3,4,5,6,7,8,9]
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

if(int(num1) in valid_nums and int(num2) in valid_nums):
    operator = input("Enter operator(+,-,*,/)")
    if(operator != '+' and operator != '-' and operator != '*' and operator != '/'):
        print("Invalid operator")
    else:
        if(operator == '+'):
            result = int(num1) + int(num2)
        elif(operator != '-'):
            result = int(num1) - int(num2)
        elif(operator != '*'):
            result = int(num1) * int(num2)
        else:
            result = int(num1) / int(num2)
    try:
        print("Result: " + str(result))
    except:
        print("")
else:
    print("Invalid Input")

    