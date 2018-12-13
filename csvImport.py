import pyodbc
import csv
import logging
import os.path
import writeCsv
import insertRecords
from insertRecords import insert_records
from sftpGet import getSftp

# DESTINATION CONNECTION
 
my_cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; SERVER=uao-nebula; DATABASE=Staging; Trusted_Connection=yes')
my_cursor = my_cnxn.cursor()

save_here = 'C:/Users/bkt5031/Desktop/pythonAngular' 
table = '[STAGING].[dbo].TalismaLeadCards'
mycsv = 'C://Users/bkt5031/Desktop/pythonAngular/sftpDownloaded/testThisExport.csv' # SET YOUR FILEPATH
# outputFile = os.path.splitext(mycsv)[0] + "_modified.csv"


getSftp()
insert_records(table, mycsv, my_cursor, my_cnxn)
writeCsv.writeNewCsv(mycsv)
my_cursor.close()
logging.info('Data Successfully Inserted')
print('Data Successfully Inserted')