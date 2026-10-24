from typing import List

def read_integers() -> List[int]:
    userInt = input()
    intList = list(userInt.split(','))
    for i in range(len(intList)):
        intList[i] = int(intList[i])
    return intList

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
