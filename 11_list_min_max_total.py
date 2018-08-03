#리스트에서 가장 작은 수, 큰수, 합계구하기

#1. 가장작은수
a = [38,21,53,62,19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)

#2. 가장큰수
a = [38,21,53,62,19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)

#3. 합계구하기
a = [38,21,53,62,19]
total = 0
for i in a:
    total += i

print(total)

# min , max 함수 사용해서 최소값, 최대값 구하기
a = [38,21,53,62,19]
print('최소값 : {0} 최대값 : {1}'.format(min(a), max(a)))

# sum 함수 사용해서 합계구하기
a = [38,21,53,62,19]
print('합계 : {0}'.format(sum(a)))