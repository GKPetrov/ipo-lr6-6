import random
pairs_list = [[random.randint(-10, 10) for i in range(1,5)] for i in range(1,21)]
unique = []
for pair in pairs_list:
    if pair not in unique:
        unique.append(tuple(pair))
print(unique)
n = int(input("Vvedi chislo"))
count = 0
sum = 0
for i in range(len(pairs_list)):
    for j in range(len(pairs_list[i])):
        sum += pairs_list[i][j]
    if sum < n:
        count += 1
print(count)
