a = int(input())
if (a>=90) and (a<=100):
    print('A')
elif (a>=80) and (a<90):
    print('B')
elif (a>=70) and (a<80):
    print('C')
elif (a>=60) and (a<70):
    print('D')
else:
    print('F')
    
# 파이썬에서는 &&를 쓰지 않고 and 를 쓴다
# 비교할때 괄호도 해줘야 한다
# input은 str으로 받으니 정수와 비교할때는 int()를 해줘야 한다