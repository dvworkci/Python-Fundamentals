# 2D Lists & Nested Loops in Python
numberGrid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(numberGrid[0][0]) # 1
# print(numberGrid[0][1]) # 2
# print(numberGrid[0][2]) # 3

# Parsing through a 2D list using nested loop
for row in numberGrid:
    for col in row:
        print(col)