# Return statement
def cube(num):
    return num * num * num 

number = input("Enter a number: ")
result = cube(int(number))
print("Cube of " + str(number) + ": " + str(result))