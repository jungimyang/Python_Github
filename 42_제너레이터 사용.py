'''
제네레이터는 이터레이터를 생성해주는 함수.
이터레이터는 클래스에 __iter__, __next__ 또는 __getitem__ 메서드를 구현해야 하지만
제네레이터는 함수 안에서 yield라는 키워드만 사용하면 끝
'''


def number_generator(stop):
    n = 0  # 숫자는 0부터 시작
    while n < stop:  # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
        yield n  # 현재 숫자를 바깥으로 전달
        n += 1  # 현재 숫자를 증가시킴


for i in number_generator(3):
    print(i)


#  문자열을 대문자로 변환하여 함수 바깥으로 전달
def upper_generator(x):
    for i in x:
        yield i.upper()  # 함수의 반환값을 바깥으로 전달


fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)