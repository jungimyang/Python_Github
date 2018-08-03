'''표준 입력으로 삼각형의 높이가 입력됩니다.
입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요
         *
        ***
       *****
'''
a = int(input())
for i in range(a):
    for j in reversed(range(a)):
        if j > i:
            print(' ',end='')
        else:
            print('*',end='')
    for j in range(a):
        if j < i:
            print('*',end='')
        else:
            print(' ',end='')
    print()

