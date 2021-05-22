


jsonUrl = 'http://www.ibtk.kr/ifbcBodySizeMale/cfa68960fa48ac6382a509a9fa207f8f?model_query_pageable={enable:true,pageNumber:0,pageSize:9999}'

from pandas.io.json import json_normalize
import xlsxwriter
import requests
import pandas as pd
pd.set_option('display.max_rows', None)
import json
from collections import OrderedDict
from itertools import islice
from openpyxl import load_workbook

# 정상 여부 확인
response = requests.get(jsonUrl)
response

# 결과 : <Response [200]>

# JSON 데이터 획득
json = response.json()
df = pd.json_normalize(json['content'])

excel_dir = "C:/Users/dof07/Desktop/바지사이즈_hhh/colNames.xlsx"
df_from_excel = pd.read_excel(excel_dir)

for i in range(df_from_excel.shape[0]):
    for j in range(df.shape[1]):
        if df.columns[j] == str(df_from_excel.loc[i,"codeNo"]):
            df.rename(columns={df.columns[j]: str(df_from_excel.loc[i,"코드번호"])+"("+str(df_from_excel.loc[i,"codeNo"])+")"}, inplace=True)

## XlsxWriter 엔진으로 Pandas writer 객체 만들기
writer = pd.ExcelWriter('C:/Users/dof07/Desktop/바지사이즈_hhh/pandas_xlsxWriter.xlsx', engine='xlsxwriter')
## DataFrame을 xlsx에 쓰기
df.to_excel(writer, sheet_name='Sheet1')
## Pandas writer 객체 닫기
writer.close()
