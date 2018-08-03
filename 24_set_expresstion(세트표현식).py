'''
* 세트표현식 사용
{식 for 변수 in 반복가능한객체}
set(식 for 변수 in 반복가능한객체)
'''

# set 표현식 사용

a = {i for i in 'apple'}
print(a) #{'a', 'l', 'e', 'p'} 이 출력

# if 조건문을 사용한 set 표현식

a = {i for i in 'apple' if i not in 'pl'}
print(a) #{'e', 'a'} p와 l이 삭제된 나머지 문자가 출력

