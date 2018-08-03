'''
* 특정 문자가 들어있는 단어 찾기

words.txt 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요.
단어를 출력할 때는 등장한 순서대로 출력해야 하며 ,(콤마)와 .(점)은 출력하지 않아야 합니다.

'''
#text = 'Just so, you might say to them: "The proof that the little prince existed is that he was charming, that he laughed, and that he was looking for a sheep. If anybody wants a sheep, that is a proof that he exists." And what good would it do to tell them that? They would shrug their shoulders, and treat you like a child. But if you said to them: "The planet he came from is Asteroid B-612," then they would be convinced, and leave you in peace from their questions. '

#with open('word2.txt','w') as file:
#    file.writelines(text)

with open('word2.txt','r') as file:
    words = file.readline().split()
    for i in words:
        if 'c' in i != False: #c를 포함하는지 판단하기위해  'c' in 단어와 같이 in 연산자를 사용
            print(i.strip(',.'))


