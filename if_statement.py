# if statements in python
isMale = True
isTall = True

if(isMale and isTall):
    print("You are a Male and Tall")
elif(isMale and not(isTall)):
    print("You are a Short Male")
elif(not(isMale) and isTall):
    print("You are not a Male but are Tall")
else:
    print("You are neither a Male nor Tall")

# If Statements and Comparisons
def max_num(num1,num2,num3):
    if(num1 >= num2 and num1 >= num3):
        return num1
    elif(num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3
    

print(max_num(12121,2343,345))