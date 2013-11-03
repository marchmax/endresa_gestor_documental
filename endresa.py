import os
import shutil
import MySQLdb

def dir_list2(dir_name, *args):
    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if len(args) == 0:
                fileList.append(file)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    fileList.append(dirfile)
    return fileList

if __name__ == '__main__':
	llista = dir_list2('/home/march/Projectes/python/tempproves/')
	os.chdir('/home/march/Projectes/python/tempproves/')
	path = '/home/march/Projectes/python/tempproves/'
	for f in llista:
		print f
		filecurt = f.split("_",1)
		print filecurt[0]

		if (filecurt[0] != f):
			if len(filecurt[0]) < 8:
				print "Connectem a la base de dades i busquem el nif"
				codi = int(filecurt[0])
				print codi
				# Open database connection
				db = MySQLdb.connect("localhost","root","xeix30D40","temp" )
				cursor = db.cursor()
				sql = "SELECT * FROM proves WHERE codi = '%d'" %(codi)
				try:
					cursor.execute(sql)
					data = cursor.fetchone()
					print data
					nif = data[2]
					if os.path.exists(nif) == False:
						os.mkdir(nif)
						print "direcori creat amb '%s'" %(nif)

					if os.path.exists(nif) == True:
						src = os.path.join(path,f)
						dst = os.path.join(path,nif,f)
						shutil.move(src,dst)
						
				except:
					print "Error: unable to fecth data"

				# disconnect from server
				db.close()
			else:
				if os.path.exists(filecurt[0]) == False:
					os.mkdir(filecurt[0])
					print filecurt[0]

				if os.path.exists(filecurt[0]) == True:
					src = os.path.join(path,f)
					dst = os.path.join(path,filecurt[0],f)
					shutil.move(src,dst)
		else:
			print "Nom de fitxer no ortodoxe";
