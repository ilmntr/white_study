
T = int(input())

for i in range(T):
    A,B = map(int,input().split())
    print(A+B)

















# for _ in range(t):  # t 만큼 반복
# for반복문은 [ for 변수 in iterable자료형 ] 형태로 첫째줄을 작성할 수 있다.
# 이때, 반복 가능한 iterable 자료형의 요소 하나하나를 for문 안에서 사용해야 한다면 for과 in사이의 변수에 선언해서 이용할 수 있다.
# 그런데 이번 문제는 테스트 케이스로 입력받은 수 t만큼 반복을 하는 것이 중요하고 range 함수로 생성된 숫자 요소를 변수로 선언하여 사용할 필요는 없다. 
# 이런 경우 for과 in 사이를 언더바 ( _ )로 표현하는 것도 가능하다. 





# =============================================

# num = int(input())
# arr = list()
# for i in range(0,num):
#     arr.append(input())
#     arr.append(input())
# for j in range(0,num):
#     result = arr[(2*j)]+arr[(j*2+1)]
#     print(result)
    
    
    
    
    
    
    
    # numbers = list(map(int, input().split())) ->
    # static int numbers = list(map(int, input().split()))  안됨...
    # arr = list()
    #1 arr.insert((i,(i+num)),int(input().split()))
    #2 (arr[i],arr[(i+num)]) = map(int,input().split())   arr.insert....