'''
* 함수만들기 및 사용

- 함수 내부 호출 순서
1.파이썬 스크립트 최초 실행
2. hello 함수 호출
3. hello 함수 실행
4. print 함수 실행 및 'Hello, world!' 출력
5. hello 함수 종료
6. 파이썬 스크립트 종료

'''

# Hello world 출력하는 함수 만들기

def Hello():
    print('Hello World')

Hello() # 함수 호출시 -> Hello World 값이 출력

# 내용이 없는 함수 만들기

def Empty():
    pass

Empty() #아무내용이 없음

# 덧셈 함수 만들기

def add(a,b): # 매개변수(parameter) 지정
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    print(a + b)

add(30,40)
print(add.__doc__) #독스트링 출력 -> 이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다.

# 함수 결과 반환하기 (return 사용)
#return을 사용하면 값을 함수 바깥으로 전달할 수 있고, 함수에서 나온 값을 변수에 저장할 수 있다.
# return으로 반환하는 값은 반환값 이라고 하는데 함수를 호출해준 바깥에 결과를 알려주기 위해 사용

def add(a,b):
    return a + b

x = add(30,10)
print(x)

# 다중 값 반환하기 (return 사용)

def add_sub(a, b):
    return a + b, a - b

x, y = add_sub(50, 30) #튜플이 변수 여러 개에 할당(언패킹).
print('a + b 값을 반환 --> {0}, a - b 값을 반환 --> {1}'.format(x, y))

