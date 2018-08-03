# 경로에서 특정 파일이름 추출하기

# 1. split 함수와 reverse 함수로 python.exe 출력하기

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
x.reverse()

print(x[0]) # python.exe 출력

# 2. rfind 함수 사용하여 출력하기
print(path[path.rfind('\\')+1 :])

# 3. 표준 입력으로 문자열이 입력됩니다. 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만들기

words = input('문자열을 입력하세요 : ').split()
count = 0
for i in words:
    if i.strip(',.') == 'the':
        count += 1

print('the의 갯수는 --> {0}'.format(count))
