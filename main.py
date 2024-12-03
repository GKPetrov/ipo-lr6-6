import random
a = [[random.randint(-10, 10) for i in range(1,5)] for i in range(1,21)]
unique=[]
for pair in a:
    if pair not in unique:
        unique.append(tuple(pair))
print(unique)
n=int(input("Vvedi chislo"))
count=0
sum=0
for i in range(len(a)):
    for j in range(len(a[i])):
        sum+=a[i][j]
    if(sum<n):
        count+=1
print(count)