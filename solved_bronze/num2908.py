(a,b) = map(str,input().split())
aa = a[::-1]
bb = b[::-1]
if (aa>bb):
    max = aa
else:
    max = bb
print(max)



# print(max(aa,bb))
# aa = reversed(a)    <-안되는 원인 ㅆ


'''
string = 'Hello, World!'
reversed_str = ''
for i in string:
    reversed_str = i + reversed_str


string = 'Hello, World!'
reversed_str = "".join(reversed(string))


string = 'Hello, World!'
reversed_str = string[::-1]


;;;

list.append( x ) : 리스트의 끝에 항목을 추가하십시오. ( a[len(a):] = [x] )

list.extend( iterable ) : iterable의 모든 항목을 추가하여 목록을 확장 해당합니다. ( a[len(a):] = iterable )

list.insert( i, x ) : 주어진 위치에 항목을 삽입합니다. 첫 번째 인수는 삽입하기 전에 요소의 인덱스이므로 a.insert(0, x)는 목록의 앞에 삽입 합니다. 그리고 a.insert(len(a), x)와 a.append(x)는 동일하게 끝에 추가 합니다.

list.remove( x ) : 리스트에서 값이 X인 첫 번째 항목을 제거 합니다. 해당 항목이 없으면 오류입니다.

list.pop( [ i ] ) : 리스트 내의 지정된 위치에 있는 아이템을 삭제하고, 그것을 반환합니다. 인덱스를 지정하지 않으면 a.pop()은  리스트의 마지막 항목을 제거하고 반환합니다. ( 메소드 인자에서 i 를 둘러싼 대괄호는 매개 변수가 선택적이라는 것을 뜻합니다. 그 위치에 대괄호를 입력해야하는 것은 아닙니다.이 표기법은 Python Library Reference에서 자주 볼 수 있습니다.)

list.clear( ) : 리스트에서 모든 항목을 제거합니다.( del a[:] )

list.index( x [, start [, end ] ] ) : 리스트에서 값이 x 인 첫 번째 항목의 인덱스를 반환합니다. 인덱스는 0부터 시작 합니다. 그러한 항목이 없는 경우 ValueError 를 발생시킵니다. 선택적 인수 start 와 end 는 특정 하위 시퀀스로 검색을 제한하는데 사용됩니다. 반환된 인덱스는 전체 시퀀스의 시작 부분을 기준으로 계산 됩니다.

list.count( x ) : x가 리스트에 나타나는 회수를 반환합니다.

list.sort( key = None , reverse = False ) : 리스트의 항목을 정렬합니다.

list.reverse( ) : 리스트의 요소들의 순서를 뒤집습니다.

list.copy( ) : 리스트의 얕은(shallow) 카피를 돌려줍니다. a[:]와 동일합니다.


'''