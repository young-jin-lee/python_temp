
import os
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [10, 6]
pd.options.display.max_columns = 999

### cars04

excel_dir = r"C:\Users\dof07\Desktop\빅데이터분석기사실기준비\내자료\midterm_practice"
cars04 = pd.read_csv(excel_dir + "\cars04.csv")

# Data exploration

cars04.describe(include='all')
cars04.columns
cars04.shape
cars04.head()
cars04.info()
numeric_cols_temp = cars04._get_numeric_data().columns
bool_cols = cars04._get_bool_data().columns
bool_cols
numeric_cols = list(set(numeric_cols_temp) - set(bool_cols))
numeric_cols
non_numeric_cols = list(set(cars04.columns) - set(numeric_cols))
non_numeric_cols

cat_outlier_check = [{col : cars04[col].unique()} for col in non_numeric_cols if cars04[col].dtype != 'object']
cat_outlier_check

# drop rows for cat outliers
cars04['ncyl'].value_counts()
cars04.drop(cars04.loc[cars04['ncyl'] == -1].index, inplace=True)

# Data transformation : change the data type of ncyl from integer to category
cars04['ncyl'] = cars04['ncyl'].astype('category')

# NA
cars04.isnull().values.any()
cars04.isnull().sum()
cars04.isnull().sum().sum()

cars04['city_mpg'].fillna(cars04['city_mpg'].mean() , inplace=True)
cars04['hwy_mpg'].fillna(cars04['hwy_mpg'].mean() , inplace=True)
cars04['weight'].fillna(cars04['weight'].mean() , inplace=True)
cars04['wheel_base'].fillna(cars04['wheel_base'].mean() , inplace=True)
cars04['length'].fillna(cars04['length'].mean() , inplace=True)
cars04['width'].fillna(cars04['width'].mean() , inplace=True)

# Outlier

plt.boxplot(cars04['city_mpg'])



# logical fields true 값들은 몇개인가

[[cars04[col].value_counts()] for col in bool_cols]

# cyl 개수 별로 무게는 얼마나 차이가 나는가. 가장 무게가 많이 나가는 cyl 값은 ?
grouped_cyl = cars04['weight'].groupby(cars04['ncyl'])
grouped_cyl.mean()
np.nanmax(grouped_cyl.mean())

# 스포츠카와 스포츠카가 아닌 것의 딜러코스트는 어떻게 차이가 나는가
grouped_sports = cars04['dealer_cost'].groupby(cars04['sports_car'])
grouped_sports.mean()

# horsepower가 가장 높은 5개의 케이스
cars04.sort_values(by=['horsepwr'], ascending=False).head(5)

# 비주얼 빈 cut & quantile의 조합(dealer cost)


dealer_labels = ['plow25pec', 'pnormal', 'phigh25pec']
pd.qcut(cars04['dealer_cost'], q=3, labels = None)
cars04['bin_dealer_cost'] = pd.qcut(cars04['dealer_cost'], q=3, labels = dealer_labels)
cars04['bin_dealer_cost'].value_counts()
cars04["dealer_cost"].groupby(cars04['bin_dealer_cost']).agg(['count','mean','std','min','max'])

dealer_labels2 = ['small', 'medium', 'large']
pd.cut(cars04['dealer_cost'], bins=3, labels = None, right = False, include_lowest=False)
cars04['bin_dealer_cost2'] = pd.cut(cars04['dealer_cost'], bins=3, labels = dealer_labels2, right = True, include_lowest=True)
cars04['bin_dealer_cost2'].value_counts()
cars04["dealer_cost"].groupby(cars04['bin_dealer_cost2']).agg(['count','mean','std','min','max'])

pd.cut(np.array(range(10)), bins=3, labels = None, right=True, include_lowest=False)
pd.cut(np.array(range(10)), bins=3, labels = None, right=False, include_lowest=False).value_counts()

pd.qcut(np.array(range(10)), q=3, labels = None)
pd.qcut(np.array(range(10)), q=3, labels = None).value_counts()


# weight가 상위 10%와 하위 10%의 가격 차이
pd.qcut(cars04['weight'], q = [0, 0.1, 0.9, 1], labels = None)
cars04['bin_weight'], bin_edges_weight = pd.qcut(cars04['weight'],
                                                 q = [0, 0.1, 0.9, 1],
                                                 labels = ["low10pec", "mid80pec", "high10pec"],
                                                 retbins = True)
cars04['bin_weight'].value_counts()
cars04['weight'].groupby(cars04['bin_weight']).agg(['count','mean','std','min','max'])
cars04['weight'].groupby(cars04['bin_weight']).mean()['high10pec'] - cars04['weight'].groupby(cars04['bin_weight']).mean()['low10pec']

# dodge만 뽑아
cars04[cars04['name'] == 'Dodge']
cars04[cars04['name'].str.contains('Dodge')]

# 브랜드별로 평균 가격은 어떻게 되는지, 내림차순으로 정렬
cars04[['brand', 'model']] = cars04['name'].str.split(" ", 1, expand = True)
cars04['dealer_cost'].groupby(cars04['brand']).mean().sort_values(ascending=False)


#### census

census = pd.read_csv(excel_dir + "\census-retail.csv")
census.head()
cols = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
excluded_cols = [col for col in census.columns if col not in cols ]
melted_census = pd.melt(census, id_vars='YEAR', value_vars= cols, var_name="MONTH", value_name="value")
melted_census.head()

#### immigration

immigration = pd.read_csv(excel_dir + "\immigration.csv")
immigration.head()
immigration.describe()
immigration.info()
immigration['party'].unique()

immigration['party'].str.split(" ", 1, expand = True)

### life

