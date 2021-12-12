arr = input()
arr = arr.lower()
name = list()
result = list()
for i in range(97,123):
    name.append(arr.count(chr(i)))
for j in range(26):
    if(name[j]==max(name)):
        result.append((j+65))
if(len(result)>1):
    print("?")
else:
    print(chr(result[0]))
    
    
    
#     rest_list = list(filter(lambda x: test_list[x] == 3, range(len(test_list))))

# print(rest_list)
    
    
    # https://bill1224.tistory.com/228     참고
    # https://ming-jee.tistory.com/121    참고    