'''
class 이터레이터이름:
    def __getitem__(self, 인덱스):
        코드
'''

#Counter 이터레이터를 인덱스로 접근할 수 있다.
class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError


print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end=' ')