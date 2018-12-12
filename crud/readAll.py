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

#SQL Query  
SQLCommand = ("SELECT * FROM [STAGING].[dbo].[TalismaLeadCards]")  
#Processing Query  
cursor.execute(SQLCommand)   
i=1  
for rows in cursor.fetchall():  
    print("------------CRM Imports %d-----------------"%i)  
    for field in rows:  
        print(str(field))  
    print("---------------------------------------")  
    print('')  
    i=i+1  
  
#closing connection  
sql_conn.close()  