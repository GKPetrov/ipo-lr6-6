import random
pairs_list = [[random.randint(-10, 10) for i in range(1,5)] for i in range(1,21)]
unique = []
for pair in pairs_list:
    if pair not in unique:
        unique.append(tuple(pair))
print(unique)
n = int(input("Введи число"))
count = 0
sum = 0
for i in pairs_list:
    for j in i:
        sum += j
    if sum < n:
        count += 1
print(count)
