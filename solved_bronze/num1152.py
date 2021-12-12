'''
cnt = 0
sen = list()
sen.insert(0,str(input()))
for i in range(0,len(sen)):
    if((sen[i]==' ') and (sen[i+1]).isalpha()==True):
        cnt=+1
print(cnt)
'''







n = input().split()
print(len(n))


# split 함수는 띄어쓰기단위로 한문자열을 나누어 리스트로 구분해준다









# cnt = 0
# sen = list()
# sen.insert(0,input())
# for i in sen:
#     print(i)
#     print()