def add_two_numbers() -> int:
    intSum = 0
    intList = input()
    intList = intList.split(',')
    for i in intList:
        intSum += int(i)
    return intSum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
