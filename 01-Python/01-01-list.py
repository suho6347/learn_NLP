"""
파이썬에 대해 알아보자!

숫자나 단어, 문장 등을 의미있게 집합시키기 위해
파이썬에서는 list라는 자료형을 사용합니다.
"""

# 초급 ☆
# 간단하게 list가 무엇인지 아는정도

#홀수를 담은 list
odd = [1, 3, 5, 7, 9]
print(odd)

#문자를 담은 list
char = ['a', 'b', 'c']
print(char)
#Python에서는 'a'와 "a"를 다르지 않다고 인식합니다.
#즉, '(따옴표)와 "(쌍따옴표) 중 어떤 것을 사용해도 괜찮습니다!

#단어를 담은 list
word = ['life', 'time', 'gold']
print(word)

#문장을 담은 list
sent = ['life is too short', 'time is a gold']
print(sent)




"""
Python을 사용할때 list는 많이 사용하게 됩니다.
특히 NLP를 배우기 위해서는 list의 강력한 기능들을 사용하면
한층 수월하게 구현할 수 있습니다.
"""

# 중급 ☆☆
# list라는 자료형의 기능을 이해하고 활용하는 정도

#list indexing
print(word[0]) # life
print(char[-1]) # c
# [](대괄호)기호를 활용하여 list안에 있는 특정 요소에 접근할 수 있습니다.
# [](대괄호) 안에 들어가는 것은 정수만 가능합니다.
# 이 정수가 의미하는 것은 "list안에서 ~번째에 있는 것을 보여줘"입니다.

#list slicing
print(word[0:2]) # ['life', 'time'] 
print(odd[3:]) # [7, 9]
# :(쌍점)을 사용하게 되면 일정 크기의 index를 한번에 가져올 수 있습니다.

#list len
print(len(word)) # 3
print(len(sent)) # 2
# NLP에서는 상당히 많은 단어나 문장을 다루게 됩니다.
# 이 과정에서 일정 조건에 따라 몇몇 단어나 문장을 생략하게 됩니다.
# 이 때, 간단히 사용할 수 있는 방법이 len()을 사용하는 것입니다.
# 대표적으로
# "문장의 길이가 51 이상은 제거"
# "단어 인식의 수가 50,000개 제한"

#list append
word.append("stone")
print(word) # ['life', 'time', 'gold', 'stone']
fruit = []
fruit.append("apple")
fruit.append("banana")
fruit.append("coconut")
print(fruit) # ['apple', 'banana', 'coconut']
# NLP를 하다보면 list에 하나씩 단어나 문장을 넣게 되는 경우가 많습니다.
# append는 이 상황에서 상당히 유용하게 사용할 수 있습니다.

#split (번외)
randomly_sent = "이것이 바로 지금부터 공부할 리스트(list)이다."
randomly_sent_list = randomly_sent.split()
print(randomly_sent_list) # ['이것이', '바로', '지금부터', '공부할', '리스트(list)이다.']
# 문장을 다루는 과정에서 띄어쓰기 단위로 단어를 잘라 list에 넣는 방법입니다.





"""
단순히 list의 기능에서 그치지 않고
Python 자체가 지원하는 확장성을 활용하면
더 빠르고 쉽게 원하는 작업을 수행할 수 있습니다.
"""

# 고급 ☆☆☆
# list를 적재적소에 다루는 정도

#list comprehension
list_comprehension = [i for i in range(20)]
print(list_comprehension) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
even = [i for i in range(20) if i % 2 == 0]
print(even) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]