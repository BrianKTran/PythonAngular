 

# import pysftp as sftp

# def getSftp():
# 	try:
# 		s = sftp.Connection('sftp.applyweb.com', username='psusftp', password='TN.oEfGj?gPQ')

# 		remotepath1='/PSU_Coalition/export3.txt'
# 		localpath1="\\\\Desktop\\pythonAngular\\testThisExport.csv"

# 		s.get(remotepath1,localpath1, preserve_mtime=True)


# 		s.close()

# 	except:
# 		print('did not connect')

# getSftp()


import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Make connection to sFTP

def getSftp():
	with pysftp.Connection('sftp.applyweb.com',
                       	username='psusftp',
                       	password='TN.oEfGj?gPQ',
                       	cnopts = cnopts
                       	) as sftp:
    		
    		file = sftp.get('PSU_Coalition/export3.txt','C://Users/bkt5031/Desktop/pythonAngular/sftpDownloaded/testThisExport.csv')
    		print(file) ## None

	sftp.close()
