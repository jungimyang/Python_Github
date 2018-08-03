'''
딕셔너리 표현식 사용하기

{키: 값 for 키, 값 in 딕셔너리}
dict({키: 값 for 키, 값 in 딕셔너리})

'''

# dict.fromkeys(keys).items()로 키-값 쌍을 구한 뒤
# 키는 변수 key, 값은 변수 value에 꺼내고 최종적으로 key와 value를 이용하여 딕셔너리를 만듬.

keys = ['a','b','c','d']
x = {key:value for key,value in dict.fromkeys(keys).items()}
print(x)

# 키만 가져오기
print({key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()})
print({key: 0 for key in dict.fromkeys(keys).keys()})

# 값을 키로 사용
print({value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()})

# 키-값 자리를 바꿈
print({value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()})

# 딕셔너리 표현식에서 if 조건문을 사용하여 삭제할 값을 제외

x = {'a':10, 'b':20, 'c':30, 'd':40}
print({key:values for key,values in x.items() if key != 'a'}) # 키값 'a'를 제외하고 출력