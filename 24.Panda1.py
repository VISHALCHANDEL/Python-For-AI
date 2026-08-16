# Data Frames in Pandas

import pandas as pd

std_data = [(1, 'vishal', 23, 'male', 'hamirpur'),
            (2, 'ravi', 24, 'male', 'delhi')]

df = pd.DataFrame(std_data, columns = ['stud_id','name',
                                        'age', 'gender',
                                        'address'])

print(df)

# 2nd method 

df = pd.read_csv("student.csv")

# df.head(2) ---> by default top 5
# df.tail
# df.shape
# df.columns
# df.size
# df.dtypes
# df.values
# df.index
# df.age --> will show the data of age
# df['age', 'address']
# df.loc[0]
# Select multiple rows by index lables
# df.loc[[0,2,4]]
# Select a single row by integer index
# df.iloc[0]
# Select multiple rows by integer indexes
# df.iloc[[0,2]]
# Filtering rows
# df[df['age'] > 29]
# Adding a New Coloumn to a DataFrame
# df['phone_no'] = [10, 20, 30, 40, 50]
# Todrop the coloumn number
# df = df.drop(columns = ['phone_no'])
# Rename the coloumn
# df = df.rename(columns = ('age':'student_age'))
# To delete the row the table
# df = df.drop(4)
# df.loc[4] = [5, 'pinki', 28, 'female', 'banglore']
# To upate the value in row
# df.loc[2,'student_age'] = 71
# To update at multiple locations
# df.loc[[0,2], 'address'] = ['andaman', 'nicobar']

