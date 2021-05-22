# 출력을 원하실 경우 print() 활용
# 예) print(df.head())

# 답안 제출 예시
# print(레코드 수)

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

pd.options.display.max_columns = 999
print(os.getcwd())

mtcars = pd.read_csv("data/mtcars.csv")

scaler = MinMaxScaler()
# print(mtcars['qsec'])
mtcars['qsec'] = scaler.fit_transform(np.array(mtcars['qsec']).reshape(-1,1))
# print("A", mtcars['qsec'])
# print(mtcars['qsec'].shape)
# print("B", np.array(mtcars['qsec']))
# print(np.array(mtcars['qsec']).shape)
# print("C", np.array(mtcars['qsec']).reshape(-1,1))
# print(np.array(mtcars['qsec']).reshape(-1,1).shape)
# print(scaler.fit_transform(np.array(mtcars['qsec']).reshape(-1,1)))

print("result" , (mtcars['qsec'] > 0.5).sum())


