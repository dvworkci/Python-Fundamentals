# Exponent function in python
def raisePower(baseNum,powNum):
    result = 1
    for index in range(powNum):
        result = result * baseNum
    return result

print(raisePower(5,2))