'''
arr = list()
arr.append(str(input()))
print(arr)
'''
# for i in range(8):


'''
arr = list(input().split())
cnt_a=0
cnt_b=0
for i in range(0,7):
    if((int(arr[i])+1)==int(arr[(i+1)])):
        cnt_a=+1
for j in range(0,7):
    if((int(arr[i])-1)==int(arr[(i+1)])):                    #왜 안될까여
        cnt_b=+1
if(cnt_a==7):
    print("ascending")
elif(cnt_b==7):
    print("descending")
else:
    print("mixed")
'''

# --------------------

'''
a = list(map(int, input().split()))
 
if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')
  '''  
    
# 디폴트는 오름차순 정렬해주며 내림차순 정렬시 sorted(list,reverse=True)로 사용한다.


a = list(input().split())
if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')

