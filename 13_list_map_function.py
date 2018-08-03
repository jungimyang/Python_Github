'''
 map은 리스트의 요소를 지정된 함수로 처리해주는 함수
• list(map(함수, 리스트))
• tuple(map(함수, 튜플))

'''

# float를 int 로 변환해서 변수에 저장
a = [1.1,2.1,3.4,4.5]
a = list(map(int,a))
print(a) #[1, 2, 3, 4] 정수로 출력됨

# a, b = map(int, input().split()) 해당 형태를 풀어서 사용하면 아래 내용

x = input().split()    # input().split()의 결과는 문자열 리스트
x = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = x               # 맵 객체는 변수 여러 개에 저장할 수 있음