arr = list(input())
for i in range(97,123):
    try:
        print(arr.index(chr(i)),end=" ")
    except ValueError:
        print("-1",end=" ")