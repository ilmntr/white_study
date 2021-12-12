(a,b) = map(int,input().split())
if (a==0) and (b<45):
    a=23
    b=(b+15)
elif (b<45):
    a=a-1
    b=(b+15)
else:
    b=(b-45)
print(a,b)