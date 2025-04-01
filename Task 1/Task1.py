
import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
array = sys.argv[3].split(",")

start_index = 0
length = ""

while True:
    length += array[start_index]
    start_index = (start_index + m - 1) % n
    if start_index == 0:
        break

print(length)


