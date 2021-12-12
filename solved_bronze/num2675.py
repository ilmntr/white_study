# cnt = int(input())
# for i in range(cnt):
#     rep = int(input())
#     arr = list(str(input()))
#     for j in range(len(arr)):
#         prt = arr[j]
#         for _ in range(rep):
#             print(prt,end="")
#     print()
    
    
    
    
cnt = int(input())
for i in range(cnt):
    (rep,arr) = map(str,input().split())
    arr = list(str(arr))
    for j in range(len(arr)):
        prt = arr[j]
        for _ in range(int(rep)):
            print(prt,end="")
    print()