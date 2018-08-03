'''
* 키워드 인수 사용
파이썬에서는 인수의 순서와 용도를 매번 기억하지 않도록 키워드 인수(keyword argument)라는 기능을 제공한다.
키워드 인수는 말 그대로 인수에 이름(키워드)을 붙이는 기능인데 키워드=값 형식으로 사용.

• 함수(키워드=값)

'''
# 함수 생성
def personal_info(name, age, address):
    print('이름 :', name)
    print('나이 :', age)
    print('주소 :', address)

personal_info('양정임',31,'서울시 영등포구 도림동')


# personal_info 함수를 키워드 인수 방식으로 호출.
personal_info(name='양정임', age=31, address= '서울시 영등포구 도림동')
personal_info(age=31, address= '서울시 영등포구 도림동',name='양정임') # 순서 상관 없음

# 딕셔너리를 사용해서 키워드 인수로 값을 넣는 "딕셔너리 언패킹" ( ** 애스터리스크 두개를 붙임)
# ** 를 사용하는 이유는? 딕셔너리는 키-값 쌍 형태로 값이 저장되어 있기 때문

x = {'name' : 'yangjungim', 'age' : 33, 'address' : '서울시 영등포구 문래동'}
personal_info(**x) # 키- 값 둘다 출력
personal_info(*x) # 키 값만 출력됨
personal_info(**{'name' : 'yangjungim', 'age' : 33, 'address' : '서울시 영등포구 문래동'})


# 가변인수 함수 만들기
def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])