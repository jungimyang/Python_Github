'''
Python은 집합을 표현하는 세트(set)라는 자료형을 제공
-> 합집합, 교집합, 차집합 연산이 가능

세트 = {값1, 값2, 값3}
'''

# 세트 만들기
fruits = {'orange', 'orange', 'cherry'}
fruits.update({'melon'}) #멜론추가

print(fruits)

# set(반복가능한객체) 만들기

a = set('apple')
print(a) # {'e', 'l', 'a', 'p'} 출력

b = set(range(5))
print(b) # {0,1,2,3,4}  출력

# 프로즌세트 = frozenset(반복가능한객체) <-- 내용을 변경할 수 없는 세트

c = frozenset('melon')
print(c)