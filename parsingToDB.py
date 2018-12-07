#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt
import os.path
import pyodbc
import pysftp
import urllib.parse
import numpy

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; SERVER=uao-nebula; DATABASE=Staging; uid=cfserver; pwd=cf80767468; Trusted_Connection=yes') 


#Creating Cursor  
cursor = sql_conn.cursor() 

#############Database Parameters##########  
firstName= input("Please Enter firstName:")  
middleName=input("Please Enter middleName:")  
lastName=input("Please Enter lastName:")   
##########################################  
  

#SQL Query  
SQLCommand = ("INSERT INTO [STAGING].[dbo].TalismaLeadCards([first_name], [middle_initial], [last_name]) Values (?, ?, ?)")  
# SQLCommand = ("INSERT INTO [STAGING].[dbo].TalismaLeadCards([first_name], [middle_initial], [last_name]) Values ('brian', 'k', 'tran');")  
Values = [firstName, middleName, lastName]  

#Processing Query  
cursor.execute(SQLCommand, Values)   
#Commiting any pending transaction to the database.  
sql_conn.commit()  

print("Data Successfully Inserted") 

# Query the Data
print("Getting Query") 
query = "SELECT * FROM [STAGING].[dbo].[TalismaLeadCards]"
# query1 = "SELECT * FROM [STAGING].[dbo].[TalismaLeadCards]"
# query = "insert into [STAGING].[dbo].TalismaLeadCards([first_name], [middle_initial], [last_name]) Values ('brian', 'k', 'tran');"

#Processing Query  
cursor.execute(query)   
results = cursor.fetchone()   
while results:  
    print ("id:" +  str(results[0]))  
    print ("firstName:" +  str(results[1]))  
    print ("middleName:" +  str(results[2]))  
    print ("lastName:" +  str(results[3]))  
    print()  
    results = cursor.fetchone()  


# df = pd.read_sql(query, sql_conn)
# print(df)
# df.head(5)

save_here = 'C:/Users/bkt5031/Desktop/dirPath'

filename = 'C:/CommonApp/CommonApp_Prospect.txt'
# open(filename, mode='r')

#closing connection  
sql_conn.close()  















 # SELECT * FROM [STAGING].[dbo].[TalismaLeadCards]

	# delete from  [STAGING].[dbo].[TalismaLeadCards]
	# where id > 0


	# insert into [STAGING].[dbo].TalismaLeadCards([first_name], [middle_initial], [last_name]) Values ('brian', 'k', 'tran'); 