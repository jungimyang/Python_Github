'''
동물 클래스 Animal과 날개 클래스 Wing을 상속받아
새 클래스 Bird를 작성하여 '먹다', '파닥거리다', '날다', True, True가 각 줄에 출력되게 만드세요.
'''

class Animal:
    def eat(self):
        print('eating')

class Wing:
    def flap(self):
        print('flap!')

class Bird(Animal, Wing):
    def fly(self):
        print('flying')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))
