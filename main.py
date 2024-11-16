from pandas import read_csv

dataframe = read_csv("./diabetes.csv")

diabetes_count = dataframe['Outcome'].value_counts()
diabetes_propability = round((diabetes_count[1] / diabetes_count.sum()) * 100, 2)

print(dataframe)