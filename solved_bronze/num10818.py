num = int(input())
arr = list()
for i in range(0,num):
    arr.insert(i,int(input()))
max = arr[0]
min = arr[0]
for j in range(0,num):
    if (max<arr[j]):
        max = arr[j]
    if (min>arr[j]):
        min = arr[j]
print(min,max)

#     
    
cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)
    
    
#     
    
cnt = int(input())
numbers = list(map(int, input().split()))
print(min(numbers),max(numbers))
    
    
    
    
'''
answer에 원소가 없는 상태에서,
answer[0] = 1처럼 원소를 지정할 수 없습니다.
insert 또는 append 메소드를 활용해서,
answer.insert(0, 1) (answer.append(i, 입력한 숫자)로 일반화할 수 있겠죠) 내지는 answer.append(1) (answer.append(입력한 숫자)로 일반화할 수 있겠죠)처럼 해주어야 합니다.
'''
    
# arr = [] <- null list 선언
# arr = [0]*10
# arr[0] = 10


# >> arr = range(10) >> arr [0,1,2,3,4,5,6,7,8,9] >> arr[::2] # 처음부터 끝까지 두 칸 간격으로 [0,2,4,6,8] 
# >> arr[1::2] # index 1 부터 끝까지 두 칸 간격으로 [1,3,5,7,9] 
# >> arr[::-1] # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로) [9,8,7,6,5,4,3,2,1,0] 
# >> arr[::-2] # 처음부터 끝까지 -2칸 간격으로 ( == 역순, 두 칸 간격으로) [9,7,5,3,1] 
# >> arr[3::-1] # index 3 부터 끝까지 -1칸 간격으로 ( == 역순으로) [3,2,1,0] 
# >> arr[1:6:2] # index 1 부터 index 6 까지 두 칸 간격으로 [1,3,5]
