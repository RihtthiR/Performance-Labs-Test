
n = int(input("Введите длину массива: "))
m = int(input("Введите длину шага: "))

array = [0 for i in range(n)]

print("Введите значиения массива: ")

for i in range(n):
    array[i] = int(input())

check = ""
length = ""
check_num = 0

while array[0] != check:
    check_array = []

    for i in range(0 + check_num, m+check_num):
       check_array.append(array[i%n])
    check = check_array[m-1]
    length += str(check_array[0])
    check_num += m - 1

print("Длина: " + length)


