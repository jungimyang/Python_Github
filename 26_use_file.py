'''
파일사용하기
-> 파일에 문자열 쓰기, 읽기

• 파일객체 = open(파일이름, 파일모드)
• 파일객체.write(문자열)
• 파일객체.close()

'''
# hello.txt 파일을 쓰기 모드(w)로 열기

file = open('hello.txt','w') #  파일 객체 반환
file.write('Hello, World') # 파일에 문자열 저장
file.close() # 파일 객체 닫기


# hello.txt 파일을 읽기 모드(r)로 열기

file = open('hello.txt','r')

s = file.read() # 파일에서 문자열 읽기

print('file.read() 사용 ---> {0}'.format(s))
file.close()


# with open 사용 (파일을 사용한 뒤 자동으로 파일 객체를 닫음)
with open('hello.txt','r') as file:
    s = file.read()
    print('with open 사용 ---> {0}'.format(s))


# with open 사용해서 파일에 여러줄 쓰기

with open('hello2.txt','w') as file:
    for i in range(3):
        file.write('Hello, World! {0}\n'.format(i)) #Hello, World! 0 \n Hello, World! 1 \n Hello, World! 2


lines = ['안녕하세요.\n','Python\n','양정임입니다\n']

with open('hello3.txt','w') as file:
    file.writelines(lines)

# with open + readlines 사용해서 파일에 여러줄 읽기(readlines는 한 줄씩 읽어서 리스트 형태로 가져옴)

with open('hello3.txt','r') as file:
    s = file.readlines()
    print(s) # ['안녕하세요.\n', 'Python\n', '양정임입니다\n']

# with open + readline 사용해서 파일에 여러줄 읽기(한 줄씩 순차적으로 읽으려면 readline 사용)

with open('hello3.txt','r') as file:
    line = file.readline()
    print(line.strip('\n')) # 파일에서 읽어온 문자열에서 \n 삭제
    while line != '':
        line = file.readline()
        print(line.strip('\n'))
#안녕하세요.
#Python
#양정임입니다