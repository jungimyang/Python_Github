'''
Python 객체를 파일에 저장 or 가져오기
-> Python 객체를 파일에 저장할 때는 pickle 모듈의 dump를 사용
'''

import pickle

name = 'yang'
age = 31
address = '서울시 영등포구 도림동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

# 파일을 바이너리 쓰기 모드(wb)로 만들기 --> 바이너리 파일은 컴퓨터가 처리하는 파일 형식

with open('yang.p','wb') as file:

    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

# 바이너리 파일을 읽기(rb)

with open('yang.p','rb') as file:
    name = pickle.load(file) #파일의 내용을 읽으려면 pickle 모듈의 load를 사용
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)

    print('name : {0}'.format(name)) # name : yang
    print('age : {0}'.format(age)) # age : 31
    print('address : {0}'.format(address)) # address : 서울시 영등포구 도림동
    print('score : {0}'.format(scores)) # score : {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}


