import pandas as pd 
import numpy as np 

df = pd.read_csv('file/employees_cleaned_5000.csv',encoding='latin1')

df['Gender'] = df['Gender'].replace({
    'f' : 'Female',
    'm' : 'Male',
    'OTHER' : 'Other'
})

df['PerformanceRating'] = df['PerformanceRating'].replace({
    'good' : 'Good',
    'POOR' : 'Poor'
})
df["Salary"] = np.random.randint(20000, 1000001, size=len(df))

mask = df["Phone"].astype(str).str.len() < 10
df.loc[mask, "Phone"] = "0000000000"

df['YearsOfExperience'] = np.where(df['YearsOfExperience'] < 0 , 5 , df['YearsOfExperience'])

df.to_csv('file/employees_cleaned2_5000.csv')