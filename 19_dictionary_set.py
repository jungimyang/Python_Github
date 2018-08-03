'''
** 딕셔너리 메서드
'''

 # 1. update 메서드 사용



x = {'a': 10, 'b': 20, 'c': 30}

x.update(a=100, c=3000)

print('update 메서드 사용 ---> {0} , {1}'.format(x['a'], x['b']))  # a=100,  c=20로 업데이트됨


# 2. pop 메서드 사용
#  pop(키) 또는 pop(키, 기본값)은 특정 키-값 쌍을 삭제한 뒤 값을 반환



x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

x.pop('a')

print('pop 메서드 사용 ---> {0}'.format(x))  # {'b': 20, 'c': 30, 'd': 40} <-- 'a' 키와 값이 삭제됨


 # 3. del 메서드 사용 (키와 값을 삭제, pop과 다른점은? 삭제한 값을 반환 안함)



x = {'a': 10, 'b': 20, 'c': 30}

del x['b']

print('del 메서드 사용 ---> {0}'.format(x))  # {'a': 10, 'c': 30} <-- 'b'키값이 삭제


 # 4. popitem() 은 딕셔너리에서 임의의 키-값 쌍을 삭제



x = {'a': 10, 'b': 20, 'c': 30}

x.popitem()

print('popitem() 메서드 사용 ----> {0}'.format(x))


 # 5. clear()는 딕셔너리의 모든 키-값 쌍을 삭제



x = {'a': 10, 'b': 20, 'c': 30}

x.clear()

print('clear() 메서드 사용 ---> {0}'.format(x))


 # 6. get(키) 또는 get(키, 기본값)은 딕셔너리에서 특정 키의 값을 가져옴
 # 만약 키가 없을 경우 0으로 값이 반환됨



x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print(x.get('a'))  # a의 키값인 10이 출력

print(x.get('z', 0))  # z 키가 없기 때문에 none




 # 7. setdefault(키) 또는 setdefault(키, 기본값)은 딕셔너리에 키와 값을 추가



s = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print('setdefault를 사용하여 [Key : e 와 Value : 100] 을 추가하겠다 --> {0}'.format(s.setdefault('e', 100)))

print(s)


 # 8. 튜플로 딕셔너리 만들기 dict.fromkeys(키, 값)



keys = ['a', 'b', 'c', 'd']

x = dict.fromkeys(keys)

print(x)  # {'a': None, 'b': None, 'c': None, 'd': None}

y = dict.fromkeys(keys, 100)

print(y)  # {'a': 100, 'b': 100, 'c': 100, 'd': 100}
