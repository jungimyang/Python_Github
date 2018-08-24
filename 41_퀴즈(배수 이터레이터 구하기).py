'''
특정 수의 배수를 만드는 이터레이터를 작성하세요. 배수는 0부터 지정된 숫자보다 작을 때까지 만들어야 합니다.


'''

class MultipleIterator:
    def __init__(self,stop,multiple):
        self.stop = stop
        self.multiple = multiple
        self.current = 0 # 몇 번 반복했는지를 저장해야 하므로 self.current를 만들고 0을 저장
    def __iter__(self):
        return self
    def __next__(self):
        self.current += 1 #self.current가 0부터 시작했으므로 0에 self.multiple을 곱하면 0임. 따라서 self.current를 1 증가시켜서 1부터 곱하도록 함
        if self.current * self.multiple < self.stop:
            return self.current * self.multiple #배수는 self.current와 self.multiple의 곱
        else:
            raise StopIteration


for i in MultipleIterator(20,3):
    print(i, end = ' ')
