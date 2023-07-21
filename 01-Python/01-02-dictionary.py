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




# 중급 ☆☆
# dictionary와 관련된 함수들을 이해하고 사용하는 정도

# items()
for k, v in dic.items():
    print("k : ", k, "  v : ", v)
"""
k :  a   v :  d
k :  b   v :  2
k :  c   v :  1
k :  1   v :  5
k :  2   v :  6
"""

# in
if 'd' in dic:
    print("'d' exists")
else:
    print("'d' not exists")
# 'd' not exists




# 고급 ☆☆☆
# dictionary를 활용해서
# NLP에서 주로 말하는 Vocab을 구성해보자!

# examples
text = "I like a pizza, I like a cola, I like a sugar, I like a hamburger."

##### 1. pre-processing phase
import re
text = re.sub(",", " ", text)     # text에서 ","(반점)을 " "(띄어쓰기)로 바꿔주세요.
text = re.sub("\.", " . ", text)  # text에서 "."(온점)을 " . "(띄어쓰기가 포함된 온점)으로 바꿔주세요.
text = re.sub("\s+", " ", text)   # text에서 "\s+"(2칸이상 띄워진 부분)을 " "(한칸 띄어쓰기)로 바꿔주세요.
print(text) # I like a pizza I like a cola I like a sugar I like a hamburger .

##### 2. Vocab phase
text = text.strip().split(" ")
                                # text의 양 끝부분에 쓸모없는 공백을 제거(strip)하고,
                                # " "(띄어쓰기)가 되어있는 부분으로 잘라서(split) list로 만들어주세요.

vocab = {} #vocab이라는 이름으로 dictionary를 만들겠습니다.
for word in text:
    # text라는 list에서 하나씩 가져와서 word라는 변수로 사용할 것입니다.
    if word not in vocab:
        # 가져온 word가 vocab에 넣은적 없다면 새로 넣습니다.
        vocab[word] = 1
    else:
        # 만약 이미 word가 vocab에 넣어져 있다면 해당 word라는 key값에 맞는 value를 1 증가시킵니다.
        # 이것이 의미하는 것은 같은 word를 만날때마다 1씩 증가한다는 것이고,
        # 결국 처음 text라는 문장에서 이 word가 몇 번 등장했는지 count를 계산해준다는 것입니다.
        vocab[word] += 1

print(vocab) # 지금까지 읽어진 단어들과 발생 횟수들이 dictionary에 넣어져 있습니다!
# {       'I': 4, 
#      'like': 4,
#         'a': 4, 
#     'pizza': 1, 
#      'cola': 1, 
#     'sugar': 1, 
# 'hamburger': 1,
#         '.': 1    }

