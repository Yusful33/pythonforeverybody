import pandas as pd

data = pd.read_csv('EmployeeAttrition.csv')

print(data.head())

#Below allows you to view all column names
for col in data.columns: 
    print(col) 

#Check the head of the DataFrame.
print(data.head())

#Q1: Find the number of entries/rows and columns in the data.
print("Rows", len(data), "Columns", len(data.columns))

#Q2: What is the average Monthly Income?
#The round function allows you to display only a certain amount of values after the decimal
print("Avg Montly Income", round(data["MonthlyIncome"].mean(),2))

#Q3: What is the highest amount of HourlyRate ?
print("Highest Hourly  Rate", round(data["HourlyRate"].max(),2))

#Q4: What is the Department, JobRole, MaritalStatus and OverTime of EmployeeNumber 10?
dfq4 = data[["Department","JobRole", "MaritalStatus", "OverTime", "EmployeeNumber"]]
print(dfq4.loc[dfq4['EmployeeNumber'] == 10])
#Q5: What is the Employee ID of highest MonthlyIncome paid employee?
highest_paid = data.loc[data['MonthlyIncome'].idxmax()]
print(highest_paid['EmployeeNumber'])
#Q6: What is the average(mean) DailyRate group by Age for all Employees whose age is greater than 58. (hint: use groupby function)
dfq6 = data.loc[data['Age'] > 58]
print(dfq6.groupby('Age').mean()['DailyRate'])

#Q7: How many unique EducationField are there?
print(data['EducationField'].nunique())

#Q8: What are the top 5 most common JobRole?
print(data['JobRole'].value_counts().head(5))

#Q9: How many JobRoles represented by less than 100 employees?
print(sum(data['JobRole'].value_counts()<100))

#Q10: What is the correlation between Education and JobSatisfaction?
# create new title
print(data[['Education', 'JobSatisfaction']].corr())