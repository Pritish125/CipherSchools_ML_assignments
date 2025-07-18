import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/jmitr/OneDrive/Desktop/CSE/CipherScls/Assignment 2/dataset.csv')

df['JoinDate'] = pd.to_datetime(df['JoinDate'], format='%d-%m-%Y', errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['PerformanceRating'] = pd.to_numeric(df['PerformanceRating'], errors='coerce')
df.dropna(inplace=True)

df['Tenure'] = 2025 - df['JoinDate'].dt.year

def categorize_salary(salary):
    if salary < 50000:
        return "Low"
    elif 50000 <= salary <= 90000:
        return "Medium"
    else:
        return "High"

df['SalaryCategory'] = df['Salary'].apply(categorize_salary)

avg_salary_by_dept = df.groupby('Department')['Salary'].mean().reset_index()
gender_count_by_dept = df.groupby(['Department', 'Gender']).size().unstack(fill_value=0)
avg_rating_by_dept = df.groupby('Department')['PerformanceRating'].mean().reset_index()
low_performers = df[df['PerformanceRating'] <= 2]

with pd.ExcelWriter('employee_analysis_result.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Cleaned_Data', index=False)
    avg_salary_by_dept.to_excel(writer, sheet_name='Avg_Salary_By_Dept', index=False)
    gender_count_by_dept.to_excel(writer, sheet_name='Gender_Count_By_Dept')
    avg_rating_by_dept.to_excel(writer, sheet_name='Avg_Rating_By_Dept', index=False)
    low_performers.to_excel(writer, sheet_name='Low_Performers', index=False)

plt.figure(figsize=(8, 5))
sns.barplot(x='Department', y='Salary', data=avg_salary_by_dept, palette='Blues_d')
plt.title('Average Salary by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('avg_salary_by_dept.png')
plt.show()

plt.figure(figsize=(6, 6))
df['SalaryCategory'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Salary Category Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('salary_category_distribution.png')
plt.show()
