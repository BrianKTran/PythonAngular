import pyodbc
import csv
import pandas as pd
import logging
import os.path
import writeCsv

# DESTINATION CONNECTION

my_cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; SERVER=uao-nebula; DATABASE=Staging; Trusted_Connection=yes')
my_cursor = my_cnxn.cursor()

def insert_records(table, yourcsv, cursor, cnxn):
    #INSERT SOURCE RECORDS TO DESTINATION
    mycsv = 'export3.txt' # SET YOUR FILEPATH
    outputFile = os.path.splitext(mycsv)[0] + "_modified.csv"

    # with open(yourcsv, 'rb') as csvfile, open(outputFile, 'wb') as outfile:
    with open(yourcsv) as csvfile:
        csvFile = csv.reader(csvfile, delimiter=',')
        # w = csv.writer(outfile)

        

        

        header = next(csvFile)
        headers = map((lambda x: x.strip()), header)
        # w.writerow(['first_name','middle_initial','last_name','address_line_1'])
        insert = 'INSERT INTO {} ('.format(table) + ', '.join(headers) + ') VALUES '
        
         

        for row in csvFile:
            # w.writerow(row)
            values = map((lambda x: "'"+x.strip()+"'"), row)
            my_cursor.execute(insert +'('+ ', '.join(values) +');' )
            my_cnxn.commit() #must commit unless your sql database auto-commits
            logging.info('Values Inserted') 
            print('Values Inserted')


        # dbColumns = pd.read_csv(csvFile)

        # csvFile.columns
        # print(csvFile)

        # print('File Read')
        # logging.info('File Read')