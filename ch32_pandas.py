import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia','Catherine','Cahill','James','Emily','Michael','Monica','Laura','Kevin','Jordan'],
             'score':[13,9.5,16.5,np.nan,11,20,17,np.nan,8.5,19],
             'attempts':[1,3,3,2,2,3,2,3,2,1],
             'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']}

labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(exam_data, index=labels)

# #1-1.Select the 'name' and 'score' columns from the above DataFrame
# print('########## 1-1 ##########')
# print(df[['name','score']])
#
# #1-2.Select First three rows of the DataFrame
# print('########## 1-2 ##########')
# print(df.head(3))
# print(df.iloc[:3])
#
# #1-3.Select 'name' and 'score' columns in rows 1,2,5,6 from the following data frame
# print('########## 1-3 ##########')
# print(df.iloc[[1,2,5,6]][['name','score']])
# print(df[['name','score']].iloc[[1,2,5,6]])
#
# #1-4.Select all columns whose attempts is larger than 2
# print('########## 1-4 ##########')
# print(df[df['attempts']>2])
#
# #2-1.Select the rows where the score is missing (NaN)
# print('########## 2-1 ##########')
# print(df[df['score'].isnull()])
#
# #2-2.Select the rows where number of attempts in the examination is less than 2 and score greater than 15
# print('########## 2-2 ##########')
# print(df[(df['attempts']<=2) & (df['score']>=15)])
#
# #2-3.Calculate the sum of the examination attempts
# print('########## 2-3 ##########')
# print(df['attempts'].sum())
#
# #2-4.Calculate the mean of the score
# print('########## 2-4 ##########')
# print(df['attempts'].mean())
#
# #3-1.Append a new row 'k' to DataFrame with the given values for each column
# # name:'Saya', score:17.5, attempts:2, qualify:'yes', label:'k'
# print('########## 3-1 ##########')
# df.loc['k'] = ['Saya', 17.5, 2, 'yes']
# print(df)
#
# # #3-2.Delete the new row and return the original data frame from above problem
# # print('########## 3-2 ##########')
# print(df.drop('k', axis=0))
# ## row가 삭제된 Dataframe을 반영하려면 df = df.drop('k',axis=0)
#
# #3-3.Delete 'attempts' column
# print('########## 3-3 ##########')
# print(df.drop('attempts', axis=1))
# ## attempts가 삭제된 Dataframe을 반영하려면 df = df.drop('attempts', axis=1)
#
#
# #3-4.Get the sum of score gropu by 'attempts'
# grouped = df.groupby('attempts')
# grouped.sum()

# #4. Do inner join above df and below df2
# exam2_data = {'name':['Anastasia','Catherine','Ronaldo','James','Messi','Michael','Monica','Laura','Klassen','Jonas'],
#               'score2':[11,20,16.5,np.nan,10,15,20,np.nan,8,8]}
# labels2 = ['a','b','c','d','e','f','g','h','i','j']
#
# df2 = pd.DataFrame(exam2_data, index=labels2)
#
# df3 = pd.merge(df, df2, left_on='name', right_on='name')
# print(df3)