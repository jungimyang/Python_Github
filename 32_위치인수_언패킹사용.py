'''
* 위치 인수와 리스트 언패킹 사용하기

'''

# 함수에 인수를 순서대로 넣는 방식을 위치 인수(positional argument)라고 한다.
# 즉, 인수의 위치가 정해져 있다.
print(10, 20, 30)


# 리스트 또는 튜플앞에 * (애스터리스크)를 붙여보기

def print_number(a,b,c):
    print(a)
    print(b)
    print(c)

x = [10,20,30]
print_number( *x ) # 리스트(튜플) 앞에 *를 붙이면 언패킹(unpacking)이 되어서 print_numbers(10, 20, 30)과 똑같은 동작이 된다.
print_number(*[10, 20, 30])


# 여러개의 숫자를 받고, 숫자를 각 줄에 출력하는 함수 만들기.

def print_number2(*args): # 매개변수에 *를 붙여주면 가변 인수 함수를 만들 수 있다
    for arg in args:
        print(arg)

print_number2(55)