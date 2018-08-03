
'''
표준 입력으로 숫자 두 개가 입력됩니다.
다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
그리고 세트 변수는 divisor를 사용하세요. 단, 최종 결과는 공약수의 합
입력)
10 20
결과)
18
'''

num1, num2 = map(int,input().split())

a = {i for i in range(1,num1+1) if num1 % i == 0} # 입력받은 num1 = 10의 나머지가 0인 값을 a 변수에 저장
b = {i for i in range(1,num2+1) if num2 % i == 0}

divisor = set.intersection(a,b) # 공약수를 구하려면 약수가 들어있는 두 세트(a,b) 의 교집합을 구함

result = 0

if type(divisor) == set:
    result = sum(divisor)

print(result)