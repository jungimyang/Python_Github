'''
합집합, 교집합, 차집합, 대칭차집합 사용
1) 세트1 | 세트2
2) 세트1 & 세트2
3) 세트1 - 세트2
4) 세트1 ^ 세트2
'''

# 1. a | b는 합집합(union)이며 OR 연산자 |를 사용
a = {1,2,3,4,5}
b = {2,4,8,9,10}
print('합집합---> {0}'.format(a|b)) #{1, 2, 3, 4, 5, 8, 9, 10}
print('union 사용 --> {0}'.format(set.union(a,b)))
print()

# 2. a & b는 교집합(intersection)이며 AND 연산자 &를 사용
a = {1,2,3,4,5}
b = {2,4,8,9,10}
print('교집합---> {0}'.format(a&b)) #{2, 4}
print('intersection 사용 -> {0}'.format(set.intersection(a,b)))
print()

# 3. a - b는 차집합(difference)이며 - 연산자를 사용
a = {1,2,3,4,5}
b = {2,4,8,9,10}
print('차집합---> {0}'.format(a-b)) #{1, 3, 5}
print('differnce 사용 --> {0}'.format(set.difference(a,b)))
print()

# 4. a ^ b는 대칭차집합(symmetric difference)이며 XOR 연산자 ^를 사용
a = {1,2,3,4,5}
b = {2,4,8,9,10}
print('대칭차집합---> {0}'.format(a^b)) #{1, 3, 5, 8, 9, 10}
print('symmetric_difference 사용 ---> {0}'.format(set.symmetric_difference(a,b))) #{1, 3, 5, 8, 9, 10}


