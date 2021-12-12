arr = list()
max = 0
for i in range(9):
    arr.append(int(input()))
    if(max<arr[i]):
        max = arr[i]
        cnt = i+1
print(max)
print(cnt)








'''
l=[int(input())for i in range(9)]
print(max(l),l.index(max(l))+1)
'''