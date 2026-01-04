#importing imp libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#assigning the file path
file_path= r'C:\Users\DELL\Downloads\quantum_business_adoption_dataset.csv'
df=pd.read_csv(file_path)
print(df.describe())
df.isna().sum()
print(df.info())
#filling the null values
df['QC_Investment_Million_USD']= df['QC_Investment_Million_USD'].fillna(df['QC_Investment_Million_USD'].median())
df['Quantum_Adoption_Percentage']=df['Quantum_Adoption_Percentage'].fillna(df['Quantum_Adoption_Percentage'].median())
df['Expected_Profit_Increase_Pct']=df['Expected_Profit_Increase_Pct'].fillna(df['Expected_Profit_Increase_Pct'].median())
num_duplicates = df.duplicated().sum()
print(num_duplicates)
print(df.info())
sns.histplot(data=df, x=df['QC_Investment_Million_USD'], y=df['Year'])
plt.xlabel=('Quantum investment')
plt.ylabel= ('Years')
plt.title= ("QC INVESTMENT in millions VS Years")
plt.show()
from scipy.stats import zscore
#Z- SCORE
df['Z_Score of investment']=zscore(df['QC_Investment_Million_USD'])
sns.histplot(data=df, x=df['Quantum_Adoption_Percentage'], y=df['Year'])
plt.xlabel=('Quantum_Adoption_Percentage')
plt.ylabel= ('Years')
plt.title= ("QC adoption VS Years")
plt.show()
df['Quantum_Adoption_MinMax'] = (df['Quantum_Adoption_Percentage'] - df['Quantum_Adoption_Percentage'].min()) / \
                                (df['Quantum_Adoption_Percentage'].max() - df['Quantum_Adoption_Percentage'].min())

# Check result
print(df[['Quantum_Adoption_Percentage', 'Quantum_Adoption_MinMax']].head())
# Save cleaned dataset
df.to_csv("quantum_business_adoption_clean.csv", index=False)
