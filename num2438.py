# a = int(input())

# while(not a==0):
#     i = a
#     while(not i==0):
#         print('*',end='\n')
#         i = i-1
#     print("\n")
#     a = a-1

# for i in range(4, 8):

# family = ['mother', 'father', 'gentleman', 'lady']
# for x in family:        # family의 각 항목 x에 대하여:
    # print(x, len(x))    # x와 x의 길이를 출력하라.



# a = int(input())
# for i in range(1, (a+1)):
#     for j in range(1, (i+1)):
#         print("*",end="")
#     print()
    
    

a = int(input())
for i in range(1, (a+1)):
    while(not i==0):
        print("*",end="")
        i = (i-1)
    print()
  



''' 
    inp = int(input())
for i in range(1,(inp+1)):
    print("*" * i)
 

inp = int(input())
for i in range(1, (inp+1)):
    for j in range(1, (i+1)):
        print("*",end="")
    print()
'''