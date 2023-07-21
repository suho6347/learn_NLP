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
# 참조 : https://doorbw.tistory.com/171

# 초급 ☆
# size, shape
contry = [['Angola', 'Argentina', 'Austria', 'Australia'], ['Bangladesh', 'Belgium', 'Bolivia', 'Belarus']]
contry_arr = np.array(contry)
print(len(contry)) # 2
print(contry_arr.size) # 8
print(contry_arr.shape) # (2, 4)
# 2x4 행렬이 주어졌을때, list의 'len()'같은 경우는 맨 왼쪽에 있는 2만 인식할 수 있습니다.
# 그러나 numpy array의 'size'를 사용하면 2x4 행렬의 모든 원소의 수를 계산해 줍니다.
# 심지어 'shape'를 사용하면 행렬의 형태를 바로 알려줍니다!

row, col = contry_arr.shape
print(row) # 2
print(col) # 4
# 행과 열로 나누어 인식시킬 수도 있습니다.




# 중급 ☆☆
# 이 부분에서 사용되는 것이 어떻게 작동되는지 잘 이해하셔야
# 실수 없는 Python 코딩이 완성됩니다.

# axis
arr1 = np.random.randn(5, 3) # 5x3 행렬을 만들어주세요, 안에 있는 값은 정규분포값(randn)에 따라 랜덤으로 설정합니다.
print(arr1)

print(np.sum(arr1, axis=0)) # 5x3에서 '5'부분을 압축시켜 합쳐주세요. 결과는 1x3 행렬이 됩니다.
print(np.sum(arr1, axis=1)) # 5x3에서 '3'부분을 압축시켜 합쳐주세요. 결과는 1x5 행렬이 됩니다.

print(np.sort(arr1, axis=0)) # 5x3에서 '5'부분을 기준으로 5,5,5 세로로 정렬해주세요.
print(np.sort(arr1, axis=1)) # 5x3에서 '3'부분을 기준으로 3,3,3,3,3 가로로 정렬해주세요.




# 고급 ☆☆☆
# 이 부분을 잘 이해하게 되면 
# 난이도있는 코드들을 읽을 수 있게 됩니다.

# masking
arr2 = np.random.randn(5,3)
print(arr2)

arr2_mask = arr2 > 0.5 # arr2에서 0.5이상의 값들 위치만 True인 새로운 list를 만듭니다.
print(arr2_mask)

print(arr2[arr2_mask]) # True였던 값들, 즉, 여기서는 0.5 이상인 값들을 따로 뺄 수 있습니다.

arr2[arr2_mask] = 0 # 또는 True였던 부분들을 원하는 값(여기서는 0)으로 덮어씌울 수 있습니다.
print(arr2) 