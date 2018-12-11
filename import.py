#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt
import os.path
import pyodbc
import pysftp
import urllib.parse
import numpy
import sqlalchemy as sa
from sqlalchemy import create_engine
import pymssql
import pymysql

# read CSV file
column_names = [ 'first_name', 'middle_initial', 'last_name']

# without headers
df = pd.read_csv('/Users/bkt5031/Desktop/pythonAngular/test.csv', header = None, names = column_names)
print(df)
# df = pd.read_csv('/Users/bkt5031/Desktop/pythonAngular/CommonApp_Prospect.txt', header = 0)
# print(df)
# print('Headers')
# df = pd.read_csv('/Users/bkt5031/Desktop/pythonAngular/CommonApp_Prospect.csv', header = 0)
# print(df)
# sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; SERVER=uao-nebula; DATABASE=Staging; uid=cfserver; pwd=cf80767468; Trusted_Connection=yes') 
save_here = 'C:/Users/bkt5031/Desktop/dirPath'

filename = 'C:/CommonApp/CommonApp_Prospect.txt'

# engine = create_engine('mysql://cfserver:cf80767468@myadm-sql-a02.ais.psu.edu')
# engine = create_engine('DRIVER={ODBC Driver 13 for SQL Server}; SERVER=uao-nebula; DATABASE=Staging; Trusted_Connection=yes')
engine = sa.create_engine('mssql+pymssql://uao-nebula/Staging')
with engine.connect() as conn, conn.begin():
    df.to_sql('csv', conn, if_exists='replace', index=False)

# INSERT INTO csv (`Person`, `Year`, `Company`) VALUES (%s, %s, %s)'] [parameters: (('John', 2018, 'Google')
# Creating Cursor  
 
cursor = conn.cursor()

 


#SQL Query  
# SQLCommand = ("INSERT INTO [STAGING].[dbo].TalismaLeadCards([first_name], [middle_initial], [last_name]) Values (?, ?, ?)")  
SQLCommand = ("INSERT INTO [STAGING].[dbo].TalismaLeadCards([first_name], [middle_initial], [last_name]) Values ('brian', 'k', 'tran');")  
# Values = [firstName, middleName, lastName]  

#Processing Query  
cursor.execute(SQLCommand)   
#Commiting any pending transaction to the database.  
# sql_conn.commit()  

# print("Data Successfully Inserted") 

# open(filename, mode='r')

#closing connection  
# sql_conn.close()  















 # SELECT * FROM [STAGING].[dbo].[TalismaLeadCards]

	# delete from  [STAGING].[dbo].[TalismaLeadCards]
	# where id > 0


	# insert into [STAGING].[dbo].TalismaLeadCards([first_name], [middle_initial], [last_name]) Values ('brian', 'k', 'tran'); 