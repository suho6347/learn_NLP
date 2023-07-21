"""
파이썬에 대해 알아보자!

NLP에서 단어 사전을 저장하기 위해
Python에서 제공하는 dictionary를 사용한다.
참조 : https://wikidocs.net/16
"""


# 초급 ☆
# 간단하게 dictionary를 선언하고 사용하는 정도

#dictionary 선언
dic = {}

#dictionary에 넣기 (key와 value 사용)
dic['a'] = 1
dic['b'] = 2
dic['c'] = 1
print(dic)
# {'a': 1, 
#  'b': 2,
#  'c': 1}

#dictionary에 있는거 수정하기
dic[1] = 5
dic[2] = 6
dic['a'] = 'd'
print(dic)
# {'a':'d', 
#  'b': 2, 
#  'c': 1, 
#   1 : 5, 
#   2 : 6}
#dictionary의 값에 접근하기 위해서는 기본적으로 Key를 통해야합니다.




