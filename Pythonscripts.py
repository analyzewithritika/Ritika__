# %%
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# %%
analysis_trend = pd.read_csv(r"C:\Users\rawat\Downloads\year.csv")
analysis_trend.head(17)

# %%
#plot graph
sns.barplot(x = "Year",y= "India", data= "analysis_trend", estimator="sum")


# %%
trend = pd.read_csv(r"C:\Users\rawat\Downloads\india.csv")
trend.head(100)

# %%
plt.plot(trend['Year'], trend['Enrollment_Growth_Rate(%)	'],marker='o')
plt.title('Year vs Enrollment_Growth_Rate')
plt.xlabel('Year')
plt.ylabel('Enrollment_Growth_Rate(%)	')
plt.grid(True)
plt.show()

# %%
plt.plot(trend['Year'], trend['Private Enrollments'], marker='o')
plt.title('Year vs Private Enrollments')
plt.xlabel('Year')
plt.ylabel('Private Enrollments')
plt.grid(True)
plt.show()

# %%
plt.plot(trend['Year'], trend['Public Enrollments'], marker='o')
plt.title('Year vs Public Enrollments')
plt.xlabel('Year')
plt.ylabel('Public Enrollments')
plt.grid(True)
plt.show()

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
teachers= pd.read_csv(r"C:\Users\rawat\Downloads\teachersattritiondata.csv")
teachers.head(17)

# %%
plt.plot(teachers['Year'], teachers['Public Schools (% Leaving)'], marker='o')
plt.title('Year vs leaving_rate')
plt.xlabel('Year')
plt.ylabel('Public Schools (% Leaving)')
plt.grid(True)
plt.show()

# %%
plt.plot(teachers['Year'], teachers['Private Schools (% Leaving)'], marker='o')
plt.title('Year vs leaving_rate')
plt.xlabel('Year')
plt.ylabel('Private Schools (% Leaving)')
plt.grid(True)
plt.show()

# %%
academics = pd.read_csv(r"C:\Users\rawat\Downloads\academics.csv")
academics1= pd.read_csv(r"C:\Users\rawat\Downloads\academics.csv")
academics2 = pd.read_csv(r"C:\Users\rawat\Downloads\academics.csv")

academics.head(17)
academics1.head(17)
academics2.head(17)


# %%
DATA=pd.merge(academics,academics1, on="Year")
DATA=pd.merge(academics,academics2, on="Total Students")
DATA.head()

# %%
main_data=pd.concat([academics,academics1,academics2],axis=0)
main_data.head()
academics.isnull().sum()
academics.describe()

# %%
plt.figure(figsize=(10, 6))
sns.histplot(academics['Year'], bins=30, kde=True)
plt.title('Academics by Year')
plt.show()

# %%
main_data=pd.concat([academics,academics1,academics2],axis=0)
main_data.head()
academics.isnull().sum()
academics.describe()

# %%
plt.figure(figsize=(10, 6))
sns.histplot(academics['Year'], bins=30, kde=True)
plt.title('Extracurricular performances by Year')
plt.show()

# %%
#Loading data or reading the dataset
demographics = pd.read_csv(r"C:\Users\rawat\Downloads\Demographics.csv")
demographics.head(100)

# %%
# Plotting pie charts for gender distribution of each school
for i, school in enumerate(demographics['School Name']):
    labels = ['Male', 'Female']
    sizes = [demographics['Male (%)'][i], demographics['Female (%)'][i]]
    
    plt.figure(i)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(school)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

# %%
# Plotting pie charts for Caste distribution of each school
for i, school in enumerate(demographics['School Name']):
    labels = ['General (%)','OBC (%)','SC/ST (%)',' Other(%)']
    sizes = [demographics['General (%)'][i], demographics['OBC (%)'][i], demographics['SC/ST (%)'][i], demographics['Other (%)'][i]]
    
    plt.figure(i)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(school)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

# %%
# Plotting pie charts for Religion distribution of each school
for i, school in enumerate(demographics['School Name']):
    labels = ['Hindu (%)','Muslim (%)','Sikh (%)','Christian (%)']
    sizes = [demographics['Hindu (%)'][i], demographics['Muslim (%)'][i], demographics['Sikh (%)'][i], demographics['Christian (%)'][i]]
    
    plt.figure(i)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(school)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


