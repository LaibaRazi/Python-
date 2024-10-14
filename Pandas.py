import pandas as pd


data = {
    'Name':['Laiba','Sadiya','Sameena'],
    'Age':[22,34,26],
    'Salary':[220000,23999,90000]
}

#dataframe2 
DataMakeup = {
    'Cate' : ['Eye','Lip'],
    'Brand' : ['Lakme','Loreal','J.','Khaadi']
}

# df = pd.DataFrame(DataMakeup)
# print(df)


df= pd.DataFrame(dict([(k,pd.Series(v)) for k,v in DataMakeup.items()]))

print(df)