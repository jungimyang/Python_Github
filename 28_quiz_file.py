
'''
파일을 생성하고, 10자 이하인 단어의 개수가 출력되도록 하기

'''

#words = ['anonymously\n','compatibility\n','dashboard\n','experience\n','photography\n','spotlight\n','warehouse\n']

#with open('words.txt','w') as file:
#	file.writelines(words)

with open('words.txt','r') as file:
    words = file.readlines()
    count = 0
    for i in words:
        if len(i.strip('\n')) <= 10:
            count += 1
    print(count)

