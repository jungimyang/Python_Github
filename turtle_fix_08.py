'''터틀그래픽스
turtle 모듈을 사용하여 그림을 그리기
(별그리기)
'''
import turtle as t

n, line = map(int,input().split()) #n은 모서리수, line은 선길이
t.shape('turtle')
t.speed('fastest')
t.color('pink')  # 펜의 색을 핑크색으로 설정
t.begin_fill() # 색칠할 영역 시작
for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)   # 360을 n으로 나누어서 외각을 구함
t.end_fill()  # 색칠할 영역 끝
