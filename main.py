from pandas import read_csv, DataFrame
from matplotlib import pyplot

# 讀取數據CSV檔
dataframe = read_csv("./diabetes.csv")

# 獲取不同情況的數量
entire_diabetes_count = dataframe['Outcome'].value_counts()
age_50_above_diabetes_count = dataframe[dataframe['Age'] >= 50]['Outcome'].value_counts()
age_50_below_diabetes_count = dataframe[dataframe['Age'] < 50]['Outcome'].value_counts()

# dataframe.to_excel('./糖尿病患病概率.xlsx')

# 匯總數據
entire_propability_df = DataFrame({
    '分類': ['有糖尿病', '沒有糖尿病'],
    '概率': [entire_diabetes_count[1], entire_diabetes_count[0]]
})

age_50_above_propability_df = DataFrame({
    '分類': ['有糖尿病', '沒有糖尿病'],
    '概率': [age_50_above_diabetes_count[1], age_50_above_diabetes_count[0]]
})

age_50_below_propability_df = DataFrame({
    '分類': ['有糖尿病', '沒有糖尿病'],
    '概率': [age_50_below_diabetes_count[1], age_50_below_diabetes_count[0]]
})

# print(entire_propability_df)
# print(age_50_above_propability_df)
# print(age_50_below_propability_df)

# 建立並顯示圖表
pyplot.rcParams['font.sans-serif'] = ['SimHei']
fig, axes = pyplot.subplots(nrows=1, ncols=3, figsize=(5, 5))

entire_propability_df.plot.pie(y="概率", labels=entire_propability_df['分類'], autopct='%1.2f%%', ax=axes[0])
axes[0].set_title("糖尿病整體患病率")

age_50_above_propability_df.plot.pie(y="概率", labels=age_50_above_propability_df['分類'], autopct='%1.2f%%', ax=axes[1])
axes[1].set_title("糖尿病50歲以上人士的患病率")

age_50_below_propability_df.plot.pie(y="概率", labels=age_50_below_propability_df['分類'], autopct='%1.2f%%', ax=axes[2])
axes[2].set_title("糖尿病50歲以下人士的患病率")

pyplot.show()