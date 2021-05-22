# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import matplotlib.pyplot as plt

def print_hi(name):


    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    excel_dir = "C:/Users/dof07/Desktop/바지사이즈_hhh/신체실측데이터.xlsx"
    df = pd.read_excel(excel_dir)

    print(df.shape)

    df['id'] = df.index
    df = df.iloc[:, 0:108]
    list(df.columns)
    for col in df.columns:
        print(col)

    df_tidy = df[["id", "나이(age)", "키(104)", "몸무게(510)", "넙다리둘레(419)", "허리둘레(211)", "엉덩이둘레(214)"]]
    df_tidy.head()
    df_tidy.describe()

    df_young = df_tidy[(df_tidy['나이(age)'] >= 20) & (df_tidy['나이(age)'] < 40)]

    df_young.describe()

    plt.scatter(df_young['키(104)'], df_young['몸무게(510)'])
    plt.show()


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
