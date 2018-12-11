import pyodbc


my_cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; SERVER=uao-nebula; DATABASE=Staging; Trusted_Connection=yes')
my_cursor = my_cnxn.cursor()


def insert_records(table, yourcsv, cursor, cnxn):

	with open('CommonApp_Prospect.txt') as f:
    		hours = f.read().split()
	for hour in hours:
			values = map((lambda x: "'"+x.strip()+"'"), row)
    		my_cursor.execute(insert +'('+ ', '.join(values) +');')
    		my_cnxn.commit() #must commit unless your sql database auto-commits
    		print (hour)

table = '[STAGING].[dbo].TalismaLeadCards'
mycsv = 'CommonApp_Prospect.txt' # SET YOUR FILEPATH
insert_records(table, mycsv, my_cursor, my_cnxn)
my_cursor.close()