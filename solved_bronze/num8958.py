'''
cnt = int(input())
for _ in range(cnt):
    num = 0
    result = 0
    arr = list(input().split('X'))
    for i in range(0,len(arr)):
        if(arr[i]=='O'):
            num = len(arr[i])
            num = ((1+num)*num)/2
        result = result + num
    print(int(result))
'''     

    
# PSEUDO CODE
# STACK_SAVE_O = 0
# RESULT = 0
# INPUT_STR = "OXOOXOXXX"
# FOR i IN RANGE(INPUT_STR)
#     IF INPUT_STR[i] == 'O':
#        STACK_SAVE_O += 1
#     ELSE:
#        RESULT += (STACK_SAVE_O^2 + STACK_SAVE_O) / 2
# RESULT += SIGMA(LEN(STACK_SAVE_O))


# stack = 0
# result = 0
# arr = list(input())
# for i in range(arr):
#     if arr[i] == 'O':
#         stack += 1
#     else:
#         result += ((1+stack)*stack)/2
# result += ...?





a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)






#         if (arr[j]=='O'):
#            num=+1
#         else:
#             num = ((1+num)*num)/2                  수정전 생각
#             continue



#     for j in range((len(arr)-1)):
#         if ((arr[j]=='O')and(arr[j+1]=='O')):
#             num=+1
#         elif ((arr[j]=='O')and(arr[j+1]=='X')):            다음 수정 (어림도 없지)
#             num = ((1+num)*num)/2
#             result = result + num
#         else:
#             continue


