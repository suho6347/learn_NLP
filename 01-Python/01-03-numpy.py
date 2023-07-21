import numpy as np
# numpy라는 외부 라이브러리를 사용할 것입니다.
# 근데 사용할때마다 numpy라고 길게 코딩하기 힘드니, np라고 줄여쓰겠습니다.


# numpy는 앞서 배운 list의 확장판이라고 보시면 됩니다.
# 즉, list에서 할 수 있는 것들은 numpy에서 가능할 뿐만 아니라
# list에서 할 수 없었던 추가적인 기능도 넣어졌습니다.

# list를 numpy array로 만드는 방법
animal = ['elephant', 'horse', 'monkey']
arr = np.array(animal)
print(arr) # ['elephant' 'horse' 'monkey']





# list가 못하는데 numpy array는 가능한 것
# 즉, numpy array를 쓰는 이유

# size, shape
contry = [['Angola', 'Argentina', 'Austria', 'Australia'], ['Bangladesh', 'Belgium', 'Bolivia', 'Belarus']]
contry_arr = np.array(contry)
print(len(contry)) # 2
print(contry_arr.size) # 8
print(contry_arr.shape) # (2, 4)
# 2x4 행렬이 주어졌을때, list의 'len()'같은 경우는 맨 왼쪽에 있는 2만 인식할 수 있습니다.
# 그러나 numpy array의 'size'를 사용하면 2x4 행렬의 모든 원소의 수를 계산해 줍니다.
# 심지어 'shape'를 사용하면 행렬의 형태를 바로 알려줍니다!

# example
# 주로 NLP에서 사용되는 부분은 train 과정입니다.
# 