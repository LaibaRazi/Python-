# import pandas as pd


# data = {
#     'Name':['Laiba','Sadiya','Sameena'],
#     'Age':[22,34,26],
#     'Salary':[220000,23999,90000]
# }

# #dataframe2 
# DataMakeup = {
#     'Cate' : ['Eye','Lip','Lip','Eye'],
#     'Brand' : ['Lakme','Loreal','J.','Khaadi']
# }

# # df = pd.DataFrame(DataMakeup)
# # print(df)


# df= pd.DataFrame(dict([(k,pd.Series(v)) for k,v in DataMakeup.items()]))
# print(df)
import pandas as pd

# Creating a dataset of student information
data = {
    'Student_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Ali', 'Sara', 'Ahmed', 'Zara', 'Maya', 'Omar'],
    'Age': [16, 17, 15, 16, 17, 15],
    'Gender': ['M', 'F', 'M', 'F', 'F', 'M'],
    'Math_Score': [85, 92, 78, 90, 88, None],  # Include None to simulate missing data
    'English_Score': [88, 79, 85, 91, None, 77],  # Include None to simulate missing data
    'Passed': [True, True, False, True, False, True]
}

# Creating a DataFrame
students_df = pd.DataFrame(data)

# Display the initial dataset
print("Initial Dataset:\n", students_df)

# Checking for missing values
print("\nMissing data:\n", students_df.isnull())
print("\nTotal missing values per column:\n", students_df.isnull().sum())

# Filling missing values with the mean of the respective columns
students_df['Math_Score'].fillna(students_df['Math_Score'].mean(), inplace=True)
students_df['English_Score'].fillna(students_df['English_Score'].mean(), inplace=True)

# Check the DataFrame after filling missing values
print("\nDataFrame after filling missing values:\n", students_df)

