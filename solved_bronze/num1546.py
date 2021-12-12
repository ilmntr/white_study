cnt = int(input())
num = list(map(int, input().split()))
new_num = list()
for i in range(len(num)):
    new_num.insert(i,(int(num[i])/int(max(num)))*100)
result = sum(new_num)/len(new_num)
print(result)


    # a = int(num[i])
    # b = int(max(num))
    # c = (a/b)*100
    # new_num.insert(i,c)
    
    
# new_num.insert(i,(int(num[i])/int(max(num)))*100)



# num = input().split())
# 이걸 이렇게 변경
# num = list(map(int, input().split()))
# '8' '16' 중에는 '8'이 더 크다 앞자리때매