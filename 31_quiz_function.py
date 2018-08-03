'''
표준 입력으로 숫자 두 개가 입력됩니다.
두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 출력되게 만드세요.
이때 나눗셈의 결과는 실수라야 합니다.

입력)  10 20
결과)  덧셈: 30, 뺄셈: -10, 곱셈: 200, 나눗셈: 0.5

'''
a, b = map(int,input().split())

def add_sub(a,b):
    return (a + b), (a - b), (a * b), (a / b)

add, substract, multi, divide  = add_sub(a,b)
print('덧셈 : {0}, 뺄셈 : {1}, 곱셈 : {2}, 나눗셈 : {3}'.format(add,substract,multi,divide))