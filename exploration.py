
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

excel_dir = "C:/Users/dof07/Desktop/바지사이즈_hhh/신체실측데이터.xlsx"
df = pd.read_excel(excel_dir)

print(df.shape)

df['id'] = df.index
df = df.iloc[:,0:108]
list(df.columns)
for col in df.columns:
    print(col)

df_tidy = df[["id","나이(age)", "키(104)", "몸무게(510)", "넙다리둘레(419)", "허리둘레(211)", "엉덩이둘레(214)"]]
df_tidy.head()
df_tidy.describe()

age_hist_df = pd.DataFrame(df_tidy, columns=['나이(age)'])
age_hist = age_hist_df.plot.hist(bins=30, color='c', grid=True)
age_hist.set_xlabel("age")
age_hist.set_ylabel("frequency")
age_hist.set_title("age histogram")
plt.show()

df_young = df_tidy[(df_tidy['나이(age)'] >= 20) & (df_tidy['나이(age)'] < 40)]

df_young.describe()

age_hist_df = pd.DataFrame(df_young, columns=['나이(age)'])
age_hist = age_hist_df.plot.hist(bins=30, color='c', grid=True)
age_hist.set_xlabel("age")
age_hist.set_ylabel("frequency")
age_hist.set_title("age histogram")
plt.show()

height_hist_df = pd.DataFrame(df_young, columns=['키(104)'])
height_hist = height_hist_df.plot.hist(bins=100, color='c', grid=True)
height_hist.set_xlabel("height")
height_hist.set_ylabel("frequency")
height_hist.set_title("height histogram")
plt.show()

waist_hist_df = pd.DataFrame(df_young, columns=['허리둘레(211)'])
waist_hist = waist_hist_df.plot.hist(bins=100, color='c', grid=True)
waist_hist.set_xlabel("waist")
waist_hist.set_ylabel("frequency")
waist_hist.set_title("waist histogram")
plt.show()

weight_hist_df = pd.DataFrame(df_young, columns=['몸무게(510)'])
weight_hist = weight_hist_df.plot.hist(bins=100, color='c', grid=True)
weight_hist.set_xlabel("weight")
weight_hist.set_ylabel("frequency")
weight_hist.set_title("weight histogram")
plt.show()

thigh_hist_df = pd.DataFrame(df_young, columns=['넙다리둘레(419)'])
thigh_hist = thigh_hist_df.plot.hist(bins=100, color='c', grid=True)
thigh_hist.set_xlabel("thigh")
thigh_hist.set_ylabel("frequency")
thigh_hist.set_title("thigh histogram")
plt.show()

hip_hist_df = pd.DataFrame(df_young, columns=['엉덩이둘레(214)'])
hip_hist = hip_hist_df.plot.hist(bins=100, color='c', grid=True)
hip_hist.set_xlabel("hip")
hip_hist.set_ylabel("frequency")
hip_hist.set_title("hip histogram")
plt.show()

plt.subplot(221)
plt.scatter(df_young['키(104)'],df_young['몸무게(510)'])
plt.show()

plt.subplot(222)
plt.scatter(df_young['키(104)'],df_young['허리둘레(211)'])
plt.show()

plt.subplot(223)
plt.scatter(df_young['몸무게(510)'],df_young['허리둘레(211)'])
plt.show()