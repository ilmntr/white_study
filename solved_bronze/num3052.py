'''
arr = list()
arr_div = list()
cnt = 0
for i in range(10):
    arr.insert(i,int(input()))
    arr_div.insert(i,(arr[i]%42))
for j in range(0,42):
    if(arr_div.count(j)>0):
        cnt=+1                              #  왜 안될까...
print(cnt)
'''









# arr를 set으로 집합 자료형으로 만들어준다  (set함수는 간단하게 말하면, 중복을 제거하기 위한 필터역할을 해준다.)
# set( ) 함수는 집합 자료형을 생성할 때뿐만 아니라 다른 iterable 자료형을 집합 자료형으로 변환하는데도 사용할 수 있다. 
# 위와 같이 하면 nums라는 리스트 자료형을 집합 자료형으로 변환할 수 있다.
# 집합 자료형으로 변환되면 리스트에 있던 중복되는 요소는 제거할 수 있다.

arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))