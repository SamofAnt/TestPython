
#size = int(input("Введите размер массива: "))
#k1 = 0
#k2 = 0
#k3 = 0
#array = [0] * size
#for i in range(0, size):
#    array[i] = int(input())
#for i in range(0, size):
#   for j in range(i + 1, size):
#        if array[i] < array[j]:
#            temp = array[i]
#            array[i] = array[j]
#            array[j] = temp
#for i in range(0, size):
#    if array[i] > 0:
#        k1 += 1
#    elif array[i] < 0:
#        k2 += 1
#    elif array[i] == 0:
#        k3 += 1
#print(array)
#print(f"Количество положительных: {k1}, количество отрицательных: {k2} и нулевых: {k3}")


size = 2
arr = [[0 for col in range(size)] for row in range(size)]
for i in range(0,size):
    for j in range(0, size):
        print("Enter value", i+1, " row ", j+1, "column in first array:")
        number = int(input())
        arr[i][j] = number
#for i in range(0, size):
#    for j in range(0, size):
#        print(arr[i][j], end=" ")
#    print()
#print()
#for i in range(0, size):
#    sum_row = 0
#    for j in range(0, size):
#        sum_row += arr[i][j]
#    avg = sum_row / size
#    print("Sum: ", i+1, " row ", j+1, "colums = ", {sum_row}, " and avg = ", {avg})

 #<---------№1----------->
max = arr[0][0]
for i in range(0, size):
    for j in range(0, size):
        if max < arr[i][j]:
            max = arr[i][j]
print("Max element: ", {max})
#print("Max: ", max)
#arr2 = [[0 for col in range(size)] for row in range(size)]
#for i in range(0,size):
#    for j in range(0, size):
#        print("Enter value", i+1, " row ", j+1, "column in second array:")
#        number = int(input())
#        arr2[i][j] = number
#sumArr = [[0 for col in range(size)] for row in range(size)]
#for i in range(0, size):
#    for j in range(0, size):
#        sumArr[i][j] = arr[i][j] + arr2[i][j]
#    #print("Summary array: ")
for i in range(0, size):
    for j in range(0, size):
        print(arr[i][j], end=" ")
    print()

# <---------№2----------->
print("Elements not on the main diagonal:", end=" ")
for i in range(0, size):
    for j in range(0, size):
        if i != j:
            print(arr[i][j], end=" ")
print()
 #<---------№3----------->
number = int(input("Enter value for search: "))
for i in range(0, size):
    for j in range(0, size):
        if number == arr[i][j]:
            print("Element ", number, " exists on ", i + 1, "row and ", j + 1, "column")
            break
