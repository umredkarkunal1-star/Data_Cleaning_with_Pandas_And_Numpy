import pandas as pd
import numpy as np

df = pd.read_csv('employees_raw_5000.csv',encoding='latin1')

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)


df['Age'] = df['Age'].fillna(df['Age'].mean())

df['PerformanceScore'] = df['PerformanceScore'].fillna(df['PerformanceScore'].mean())


performance_rating = ['good','bad','A+','B','excellent']
mask = df["PerformanceRating"].isna()
df.loc[mask, "PerformanceRating"] = np.random.choice(performance_rating, size=mask.sum())


joining_dates = [
    "2005-04-04",
    "2022-01-08",
    "2020-01-15",
    "2010-02-12",
    "2005-12-14"
]
mask = df["JoiningDate"].isna()
df.loc[mask, "JoiningDate"] = np.random.choice(
    joining_dates,
    size=mask.sum()
)

df['Email'] = df['Email'].fillna('unknow')

df['Phone'] = df['Phone'].fillna(0000000000)

df['YearsOfExperience'] = df['YearsOfExperience'].fillna(df['YearsOfExperience'].mean())

df['Salary'] = df['Salary'].fillna(500000)

df['Bonus'] = df['Bonus'].fillna(12000)

df.dropna(inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df['Gender'] = df['Gender'].replace({
    'male' : 'Male',
    'female' : 'Female',
    'M' : 'Male',
    'F' : 'Female',
    'other' : 'Other',
    'MALE' : 'Male',
    'FEMALE' : 'Female'
})

df['Age'] = np.where(df['Age'] < 0 , df['Age'].mean() , df['Age'])

import numpy as np

avg_salary = df["Salary"].mean()

df["Salary"] = np.where(
    (df["Salary"] > 1000000) | (df["Salary"] < 20000),
    avg_salary,
    df["Salary"]
)

df['PerformanceRating'] = df['PerformanceRating'].replace({
    'GOOD' : 'Good',
    'BAD' : 'Bad',
    'G' : 'Good',
    'B' : 'Bad',
    'g' : 'Good',
    'b' : 'Bad',
    'EXCELLENT' : 'Excellent',
    'poor' : 'Poor',
    'A' : 'Good',
    'B' : 'Bad',
    'C' : 'Average',
    'D'  : 'Poor',
    'a' : 'Good',
    'b' : 'Bad',
    'c' : 'Average',
    'd'  : 'Poor',
    'A+' : 'Good',
    'A-' : 'Average',
    'a+' : 'Good',
    'a-' : 'Average',
})

df["Department"] = df["Department"].str.title()
df["JobTitle"] = df["JobTitle"].str.title()
df["City"] = df["City"].str.title()

df.to_csv('employees_cleaned_5000.csv', index=False)





