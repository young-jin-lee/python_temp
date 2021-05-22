import itertools

# itertools.product 예제
cnt = 0
for a, b, c in itertools.product(range(3), range(3), range(3)):
    print(a, b, c)


# itertools.combination 예제
# L에서 2개로 이뤄지 가능한 모든 조합 뽑기

L = ['a', 'b', 'c', 'd']
for comb in itertools.combinations(L,2):
    print(comb)

# L에서  가능한 모든 조합 뽑기

L = ['a', 'b', 'c', 'd']
for r in range(1, len(L) + 1):
    for comb in itertools.combinations(L,r):
        print(comb)

# L에서 가능한 모든 순열 뽑기
for r in range(1, len(L)):
    for comb in itertools.permutations(L, r):
        print(comb)


# List Comprehension

L = []
for x in range(10):
    if x%2 == 0:
        L.append(x**2)

L = [x**2 for x in range(10) if x%2 == 0]

# Dictionary comprehension1
dict = dict()
for x, y in zip(range(10), range(10)):
    if x%2 == 0:
        dict[x] = y ** 2

dict = {x:y**2 for x, y in zip(range(10), range(10)) if x%2 == 0}
print(zip(range(10), range(10)))
for item in zip(range(10), range(10)):
    print(item)
print(dict)

# Dictionary comprehension2
dict2 = {1:'NaN', 2:2, 3:3, 4:'NaN'}
dict3 = {x:y for x, y in dict2.items() if y != 'NaN'}
print(dict3)


### NUMPY
import numpy as np

# 배열만들기

print(np.zeros((10,2)))

print(np.arange(1,5,0.1))

print(np.linspace(0,1,9))

### PANDAS
import pandas as pd

S = pd.Series({"a" : 1, "b": 2, "c" : 3})

import numpy as np

lst = np.array([1,2,3,4])
lst.shape
lst
lst.reshape(-1, 1)




