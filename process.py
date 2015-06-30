#!/usr/bin/python
import MySQLdb
import os

def ocr():
	file=open('converted.txt','r') #opens the file created by Tesseract
	adm = file.read()
	adm_no=adm.split("No. ",1)[1]
	adm_no=adm_no.split('\n',1)[0]
	adm=int(adm_no)
	return adm

def check(adm, db):
	cursor=db.cursor()
	sql = "SELECT * FROM voting WHERE Adm_no='%d'" % \
		(adm)
	try:
		cursor.execute(sql)
		result=cursor.fetchall();
		if result:
			print "Already Voted"
		else:
			return 1
	except:
		print "Unable to fetch data"
	
def userinput():
	choice = int(raw_input("Select (1) for Lucas and (2) for Alex"))
#	if choice==1:
#		print "Voted successfully for Lucas!"
#	elif choice==2:
#		print "Voted successfully for Alex!"
#	else:
#		print "Invalid Choice!"
	return choice

def submit(adm, choice, db):
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	# Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO voting(Adm_no, \
	       vote) \
	       VALUES ('%d','%s' )" % \
	       (adm, choice)
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	   print "Voted Successfully!"
	except:
	   # Rollback in case there is any error
	   db.rollback()
	   print "Voting unsuccesful!! :("
	
	# disconnect from server
	db.close()	

def main():
	try:
		# Open database connection		
		db = MySQLdb.connect(host="",user="",passwd="",db="" )
	except:
		print "Cannot connect to the database"
		quit()
	os.system("sh pshell.sh") //pshell.sh crops the provided image for faster image recognition
	adm=ocr()
	if (check(adm, db)==1):
		choice=userinput()
		submit(adm, choice, db)
	else:
		db.close()

if __name__=="__main__":
	main()
