#Create a Bubble Sort algorithm in Python:
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)

for i in range(n-1):
    for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)


#Improved Bubble Sort algorithm:
mylist = [7, 3, 9, 12, 11]

n = len(mylist)
i_counter = 0
j_counter = 0
counter = 0

for i in range(n-1):
    i_counter += 1
    swapped = False
    for j in range(n-i-1):
        j_counter += 1
        if mylist[j] > mylist[j+1]:
            counter += 1
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            swapped = True
    if not swapped:
        break

print("i loop = ", i_counter)
print("j loop = ", j_counter)
print("swap = ", counter)
print(mylist)

#
mylist1 = [7, 3, 9, 12, 11]

n = len(mylist)
i_counter1 = 0
j_counter1 = 0
counter1 = 0

for i in range(n-1):
    i_counter1 += 1
    for j in range(n-i-1):
        j_counter1 += 1
        if mylist1[j] > mylist1[j+1]:
            counter1 += 1
            mylist1[j], mylist1[j+1] = mylist1[j+1], mylist1[j]

print("i loop = ", i_counter1)
print("j loop = ", j_counter1)
print("swap = ", counter1)
print(mylist1)