from Tkinter import *
import MySQLdb
import tkMessageBox
from time import sleep


try:
	# Open database connection		
	db = MySQLdb.connect(host="",user="",passwd="",db="")
except:
	print "Cannot connect to the database"
	
master = Tk()
adm=0
status=0
#e = Entry(master).grid(row=0)
#e.focus_set()

def callback():
                global adm, status
		cursor=db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT * FROM TABLE_7 WHERE Adm_no='%s'" % \
		(e.get())
		try:
			cursor.execute (sql)
			result=cursor.fetchall();
			if result:
                            for row in result:
                                    Label(master, text="Admission number: ").grid(row=1, column=0)
				    Label(master, text="        ").grid(row=1, column=1)
                                    Label(master, text=row["Adm_no"]).grid(row=1, column=1)
                                    Label(master, text="Name: ").grid(row=2, column=0)
				    Label(master, text="                                                             ").grid(row=2, column=1)
                                    Label(master, text=row["Name"]).grid(row=2, column=1)	
				    Label(master, text="            ").grid(row=3, column=1)
                                    Label(master, text="Gender: ").grid(row=3, column=0)
                                    Label(master, text=row["Gender"]).grid(row=3, column=1)
                                    Label(master, text="Class: ").grid(row=4, column=0)
				    Label(master, text="           ").grid(row=1, column=1)
                                    Label(master, text=row["Class"]).grid(row=4, column=1)			
                                    Label(master, text="Status: ").grid(row=5, column=0)
                                    Label(master, text=row["Status"]).grid(row=5, column=1)
                                    adm=row["Adm_no"]
                                    status=row["Status"]
                                    return
                        else:
                            tkMessageBox.showinfo("Info", "That admission number does not exist!")
		except:
			print "Unable to fetch data"
			db.close()
def voting():
                global status
                if (status=='0' and adm!=0):    
                    cursor=db.cursor()
                    cursor.execute ("""
                                       UPDATE TABLE_7
                                       SET Status=%s
                                       WHERE Adm_no=%s
                                    """, (2, adm))
                    status=2
    		elif adm==0:
                    tkMessageBox.showinfo("Warning!", "Search for an admission number first!")                    
    		else:
                    tkMessageBox.showinfo("Warning!", "This student has already voted!")
e = Entry(master, width=30)
e.grid(row=0, column=0)

b = Button(master, text="Check", width=10, command=callback)
b.grid(row=0, column=1)

b2 = Button(master, text="Allow to vote", width=10, command=voting)
b2.grid(row=0, column=2)
					    
Label(master, text="Admission number: ").grid(row=1, column=0)
Label(master, text="-").grid(row=1, column=1)
Label(master, text="Status: ").grid(row=2, column=0)
Label(master, text="-").grid(row=2, column=1)

mainloop()
