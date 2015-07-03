#!/usr/bin/python
import MySQLdb
from time import sleep
import pygame

def gui():
	running = True
	pygame.init()
	pygame.mouse.set_visible(False)
	screen = pygame.display.set_mode((0,0), 500*500)
	screen.fill(pygame.Color(0,100,100))
	imgsize = pygame.Surface.get_size(screen)
	while running:
		for event in pygame.event.get():
		        if event.type == pygame.KEYDOWN:
		        	if event.key==pygame.K_1:
					background = pygame.image.load("1.jpg").convert()
		        	        screen.blit(background, (0, 0))
      		  		        pygame.display.update()
		        	if event.key==pygame.K_2:
					background = pygame.image.load("2.jpg").convert()
		        	        screen.blit(background, (0, 0))
      		  		        pygame.display.update()
		        	if event.key==pygame.K_3:
					background = pygame.image.load("3.jpg").convert()
		        	        screen.blit(background, (0, 0))
      		  		        pygame.display.update()
		        	if event.key==pygame.K_4:
					running=False
		        if event.type == pygame.QUIT:
	            		running = False	
	pygame.quit()
def ocr():
	file=open('converted.txt','r')
	adm = file.read()
	adm_no=adm.split("No. ",1)[1]
	adm_no=adm_no.split('\n',1)[0]
	adm=int(adm_no)
	return adm

def check(db):
	cursor=db.cursor(MySQLdb.cursors.DictCursor)
	sql = "SELECT * FROM voting"
	try:
		cursor.execute(sql)
		result=cursor.fetchall();
		for row in result:
			if row["Status"]=='2':
				return row["Adm_no"]		
		print "Already Voted!!"			
		return -1
	except:
		print "Unable to fetch data"
	
def userinput():
	choice = int(raw_input("Select (1) for Lucas and (2) for Alex"))
	return choice

def submit(adm, choice, db):
	if choice==1:
		Candidate_1=1
		Candidate_2=0
	elif choice==2:
		Candidate_2=1
		Candidate_1=0
	cursor2 = db.cursor()
	try:
	   # Execute the SQL command
	   cursor2.execute("""INSERT INTO HB_votes(Candidate_1, \
	      		      Candidate_2) \
	      		      VALUES ('%s','%s')""" , (Candidate_1, Candidate_2))
	   # Commit your changes in the database
	   db.commit()
	   print "Voted Successfully!"
	   return 1
	except:
	   # Rollback in case there is any error
	   db.rollback()
	   print "Voting unsuccesful!! :("
	   return 0

def main():
	try:
		# Open database connection		
		db = MySQLdb.connect(host="208.109.125.165",user="tagtasti_vote",passwd="silverstone547",db="tagtasti_voting" )
	except:
		print "Cannot connect to the database"
		quit()
	#os.system("sh pshell.sh")
	#adm=ocr()	
	while True:
		adm=check(db)	
		if (adm!=-1):
			gui()
			choice=userinput()
			if submit(adm, choice, db)==1:
				cursor=db.cursor()
				cursor.execute ("""
						   UPDATE voting
						   SET Status=%s
						   WHERE Adm_no=%s
						""", (1, adm))
		else:
			print"No match found! Trying again in 1 sec"
			sleep(1)

if __name__=="__main__":
	main()
