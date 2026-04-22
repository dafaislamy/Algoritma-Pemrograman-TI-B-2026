#Using the Selection sort on a Python list:
mylist = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(mylist)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    min_value = mylist.pop(min_index)
    mylist.insert(i, min_value)

print(mylist)


#The improved Selection Sort algorithm, including swapping values:
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

print(mylist)