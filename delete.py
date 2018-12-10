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
SQLCommand = ("Delete from [STAGING].[dbo].TalismaLeadCards where id=3")  
#Processing Query  
cursor.execute(SQLCommand)   
#Commiting any pending transaction to the database.  
sql_conn.commit()  
#closing connection  
sql_conn.close()  
print("Deleted Successfully")  
