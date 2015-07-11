#!/usr/bin/python
import MySQLdb
from time import sleep
import pygame
import smbus

bus = smbus.SMBus(1)
address = 0x04

def readNumber():
    number = bus.read_byte(address)
    return number

def gui(pygame, screen):
	running = True
	while running:
	        number=int(readNumber())
                if number==1:
                       running=False
                       return 1  
                elif number==2:
                       running=False
		       return 2
                elif number==3:
                       running=False
		       return 3
                elif number==4:
                       running=False
		       return 4
                elif number==5:
                       running=False
		       return 5
                elif number==6:
                       running=False
		       return 6
                elif number==7:
                       running=False
		       return 7
                elif number==8:
                       running=False
		       return 8                              
                elif number==10:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb1.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==11:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb2.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==12:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb3.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==13:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb4.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==14:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb5.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==15:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb6.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==16:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb7.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==17:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb8.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==18:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                sleep(0.05)
#	pygame.quit()
def gui2(pygame, screen):
	running = True
	while running:
	        number=int(readNumber())
                if number==1:
                       running=False
                       return 1  
                elif number==2:
                       running=False
		       return 2
                elif number==3:
                       running=False
		       return 3                            
                elif number==10:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg1.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==11:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg2.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==12:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg3.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==13:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==14:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==15:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==16:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==17:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==18:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                sleep(0.05)

def gui3(pygame, screen):
	running = True
	while running:
	        number=int(readNumber())
                if number==1:
                       running=False
                       return 1  
                elif number==2:
                       running=False
		       return 2
                elif number==3:
                       running=False
		       return 3                            
                elif number==10:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s1.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==11:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s2.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==12:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s3.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==13:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==14:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==15:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==16:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==17:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                elif number==18:
                       background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s0.png").convert()
                       screen.blit(background, (0, 0))
                       pygame.display.update()
                       number=0
                sleep(0.05)

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
		return -1
	except:
		print "Unable to fetch data"
	
def userinput(number):
	choice = number+1
	return choice

def submit(adm, choice, db):
	Candidate_1=0
	Candidate_2=0
	Candidate_3=0
	Candidate_4=0
	Candidate_5=0
	Candidate_6=0
	Candidate_7=0
	Candidate_8=0
	if choice==1:
		Candidate_1=1
	elif choice==2:
		Candidate_2=1
	elif choice==3:
		Candidate_3=1
	elif choice==4:
		Candidate_4=1
	elif choice==5:
		Candidate_5=1
	elif choice==6:
		Candidate_6=1
	elif choice==7:
		Candidate_7=1
	elif choice==8:
		Candidate_8=1
	cursor2 = db.cursor()
	try:
	   # Execute the SQL command
	   cursor2.execute("""INSERT INTO HB_votes(Candidate_1, \
	      		      Candidate_2, Candidate_3, Candidate_4, \
			      Candidate_5, Candidate_6, Candidate_7, Candidate_8) \
	      		      VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')""" ,\
 			      (Candidate_1, Candidate_2, Candidate_3, Candidate_4, Candidate_5, \
			      Candidate_6, Candidate_7, Candidate_8))
	   # Commit your changes in the database
	   db.commit()
	   print "HB Voted Successfully!"
	   return 1
	except:
	   # Rollback in case there is any error
	   db.rollback()
	   print "HB Voting unsuccesful!! :("
	   return 0

def submit2(adm, choice, db):
	Candidate_1=0
	Candidate_2=0
	Candidate_3=0
	if choice==1:
		Candidate_1=1
	elif choice==2:
		Candidate_2=1
	elif choice==3:
		Candidate_3=1
	cursor2 = db.cursor()
	try:
	   # Execute the SQL command
	   cursor2.execute("""INSERT INTO HG_votes(Candidate_1, \
	      		      Candidate_2, Candidate_3) \
	      		      VALUES ('%s','%s','%s')""" ,\
 			      (Candidate_1, Candidate_2, Candidate_3))
	   # Commit your changes in the database
	   db.commit()
	   print "HG Voted Successfully!"
	   return 1
	except:
	   # Rollback in case there is any error
	   db.rollback()
	   print "HG Voting unsuccesful!! :("
	   return 0

def submit3(adm, choice, db):
	Candidate_1=0
	Candidate_2=0
	Candidate_3=0
	if choice==1:
		Candidate_1=1
	elif choice==2:
		Candidate_2=1
	elif choice==3:
		Candidate_3=1
	cursor2 = db.cursor()
	try:
	   # Execute the SQL command
	   cursor2.execute("""INSERT INTO S_votes(Candidate_1, \
	      		      Candidate_2, Candidate_3) \
	      		      VALUES ('%s','%s','%s')""" ,\
 			      (Candidate_1, Candidate_2, Candidate_3))
	   # Commit your changes in the database
	   db.commit()
	   print "S Voted Successfully!"
	   return 1
	except:
	   # Rollback in case there is any error
	   db.rollback()
	   print "S Voting unsuccesful!! :("
	   return 0

def main():
	pygame.init()
	pygame.mouse.set_visible(False)
	screen = pygame.display.set_mode((640,480))
	screen.fill(pygame.Color(0,100,100))
	imgsize = pygame.Surface.get_size(screen)
	try:
		# Open database connection		
		db = MySQLdb.connect(host="",user="",passwd="",db="")
	except:
		print "Cannot connect to the database"
		quit()
	#os.system("sh pshell.sh")
	#adm=ocr()	
	while True:
		adm=check(db)
		if (adm!=-1):
		        background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phb1.png").convert()
		        screen.blit(background, (0, 0))
		        pygame.display.update()			
			choice=gui(pygame, screen)
			if submit(adm, choice, db)==1:
		                background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_phg1.png").convert()					
			        screen.blit(background, (0, 0))
			        pygame.display.update()
				choice=gui2(pygame, screen)
				if submit2(adm, choice, db)==1:
			                background = pygame.image.load("/home/pi/Desktop/ocr/pictures/f_s1.png").convert()					
				        screen.blit(background, (0, 0))
				        pygame.display.update()
					choice=gui3(pygame, screen)
					if submit3(adm, choice, db)==1:
				                background = pygame.image.load("/home/pi/Desktop/ocr/pictures/w1.png").convert()					
					        screen.blit(background, (0, 0))
					        pygame.display.update()					
						cursor=db.cursor()
						cursor.execute ("""
								   UPDATE voting
								   SET Status=%s
								   WHERE Adm_no=%s
								""", (1, adm))
						sleep(3)
		else:
		        background = pygame.image.load("/home/pi/Desktop/ocr/pictures/w0.png").convert()
		        screen.blit(background, (0, 0))
		        pygame.display.update()			
			sleep(1)

if __name__=="__main__":
	main()
