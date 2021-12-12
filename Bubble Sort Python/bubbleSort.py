import random

def bubbleSort (unsortedList):
    for i in range (len(unsortedList)):
        for j in range (0, len(unsortedList) - 1 - i):
            if unsortedList[j] > unsortedList[j + 1]:
                unsortedList[j], unsortedList[j + 1] = unsortedList[j + 1], unsortedList[j]
    return x

x = list(random.sample(range(100), 20))
x = bubbleSort(x)

print(x)