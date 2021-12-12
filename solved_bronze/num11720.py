cnt = int(input())
num = list(map(int, input()))
sum = 0
for i in range(len(num)):
    sum = sum + num[i]
print(sum)