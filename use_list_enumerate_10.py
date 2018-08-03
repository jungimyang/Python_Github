''' for 문으로 인덱스와 요소의 값을 동시 출력(enumerate 사용)'''

a = [34,21,53,6,19]
for index, value in enumerate(a):
    print('인덱스 : {0} 값 : {1}'.format(index, value))
