'''

    This GUI project is not a fully funmctional banking application.
    It can only insert values into the database connected to it.
    Use your credentials to login into your 
    database (here in this case MySql is used to access database).
    You are free to use this GUI to learn basics of tkinter module.
    
    

'''
from tkinter import *
import time
import mysql.connector
'''db = mysql.connector.connect(
	host = "localhost",			#hostname
	user = "unknown",			#user      use your credentials
	passwd = "#######",			#password
	database = "banking"		#mysql uses the database mentioned here
	)'''
my_cursor = db.cursor()
#my_cursor.execute("CREATE TABLE Customers (acc_No INT  PRIMARY KEY, name VARCHAR(30) NOT NULL, mob INT, pas VARCHAR(30) NOT NULL, bal INT NOT NULL)")
#already created the database;
#my_cursor.execute("DROP TABLE Customers")
db.commit()

def about():
	Root = Tk()
	Root.title("About Developer")

	about_label1 = Label(Root,text = "Developed by Abhinav Tiwari as a fun project, during COVID-19 pandemic")
	about_label2 = Label(Root,text = "made by using basics of tkinter module.")
	about_label3 = Label(Root,text = "This project uses mysql-connector for python to interact with your datatbase.")
	about_label4 = Label(Root,text = "It also uses basiic queries of mysql i.e create, insert,etc")
	about_label5 = Label(Root,text = "I will post more fun projects on my github account :->")
	about_label6 = Label(Root,text = "https://github.com/abhinav-idle/Mini-Projects")

	about_label1.pack()
	about_label2.pack()
	about_label3.pack()

	about_label4.pack()
	about_label5.pack()
	about_label6.pack()
	Root.mainloop()

def user_details(acc_no,password):
	#fetching details from database by giving acc_No and password
	#of user.

	my_cursor.execute("SELECT name,acc_No,mob,bal FROM Customers WHERE acc_No=%s AND pas=%s",(acc_no,password))
	det = my_cursor.fetchone()	#fetch returns the iterable stored in my_cursor
	
	Root = Tk()
	Root.title("Customer Info")
	Root.geometry("500x250+200+400")
	B1 = Button(Root,text = "Welcome to Tkinter bank of Python !!",fg = "#ffffff",bg = "#f69602",width = 35,padx = 20,pady = 5,command = about)
	B1.place(x=110,y=0)

	usrname_label = Label(Root,text = "Customer Name :",fg = "white",bg = "#003e51",width = 30)
	acc_label = Label(Root,text = "Account No: ",fg = "white",bg = "#003e51",width =30)
	mob_label = Label(Root,text = " Your mobile no :",fg = "white",bg = "#003e51",width =30)
	balance_label = Label(Root,text = "Available  balance :",fg = "white",bg = "#003e51",width =30)
	
	E1 = Entry(Root,width = 30,borderwidth =2)
	E2 = Entry(Root,width = 30,borderwidth =2)
	E3 = Entry(Root,width = 30,borderwidth =2)
	E4 = Entry(Root,width = 30,borderwidth =2)
	
	usrname_label.place(x=10,y=31)
	acc_label.place(x=10,y=61)
	mob_label.place(x=10,y=91)
	balance_label.place(x=10,y=121)
	
	E1.place(x=230,y=30)
	E2.place(x=230,y=60)
	E3.place(x=230,y=90)
	E4.place(x=230,y=120)
	
	# now, we'll insert details into the text entry fields 
	# associated to respective labels
	E1.insert(0,det[0])
	E2.insert(0,det[1])
	E3.insert(0,det[2])
	E4.insert(0,det[3])

	close = Button(Root,text = "QUIT",fg = "white",bg = "#009bce",command=Root.quit)
	close.place(x=220,y=143)

	Root.mainloop()






def usr(account_no,name,mob,password,bal):
	#inserting values into the database 
	
	my_cursor.execute("INSERT INTO Customers VALUES(%s,%s,%s,%s,%s)",(account_no,name,mob,password,bal))	
	db.commit()	

	#commit is important to save the values inserted into the database.

#Code to register customer
def register():

	Root = Tk()
	Root.title("User Registration")
	Root.geometry("500x250+200+400")
	B1 = Button(Root,text = "Welcome to Tkinter bank of Python !!",fg = "#ffffff",bg = "#f69602",width = 35,padx = 20,pady = 5,command = about)
	B1.place(x=110,y=0)

	usrname_label = Label(Root,text = "Customer Name :",fg = "white",bg = "#003e51",width = 30)
	acc_label = Label(Root,text = "Account No: ",fg = "white",bg = "#003e51",width =30)
	mob_label = Label(Root,text = " Enter your mobile no :",fg = "white",bg = "#003e51",width =30)
	password_label = Label(Root,text = "Enter your password :",fg = "white",bg = "#003e51",width =30)
	balance_label = Label(Root,text = "Enter balance to deposit :",fg = "white",bg = "#003e51",width =30)
	
	E1 = Entry(Root,width = 35,borderwidth =2)
	E2 = Entry(Root,width = 35,borderwidth =2)
	E3 = Entry(Root,width = 35,borderwidth =2)
	E4 = Entry(Root,width = 35,borderwidth =2)
	E5 = Entry(Root,width = 35,borderwidth =2)
	
	usrname_label.place(x=10,y=31)
	acc_label.place(x=10,y=61)
	mob_label.place(x=10,y=91)
	password_label.place(x=10,y=121)
	balance_label.place(x=10,y=151)
	
	E1.place(x=225,y=30)
	E2.place(x=225,y=60)
	E3.place(x=225,y=90)
	E4.place(x=225,y=120)
	E5.place(x=225,y=150)

	reg = Button(Root,text = "Register User",fg = "white",bg = "#009bce",command =lambda : usr(E2.get(),E1.get(),E3.get(),E4.get(),E5.get()))
	reg.place(x=200,y=180)

	Root.quit()
	Root.mainloop()



def login():

	Root = Tk()
	Root.title("Login window!!!!!")
	Root.geometry("500x250+200+400")
	B1 = Button(Root,text = "Welcome to Tkinter bank of Python !!",fg = "#ffffff",bg = "#f69602",width = 35,padx = 20,pady = 5,command = about)
	B1.place(x=110,y=0)

	
	acc_label = Label(Root,text = "Enter account_no	",fg = "white",bg = "#003e51")
	pass_label = Label(Root,text = "Enter your password	",fg = "white",bg = "#003e51")
	
	E1 = Entry(Root,width = 30)
	E2 = Entry(Root,width = 30)
	
	acc_label.place(x = 15,y = 41)
	pass_label.place(x = 15,y = 71)
	
	E1.place(x = 247,y = 40)
	E2.place(x = 247,y = 70)
	
	log = Button(Root,text = "Login !!",fg = "white",bg = "#009bce",command = lambda :user_details(E1.get(),E2.get()))
	log.place(x = 220, y = 100)
	
	Root.mainloop()

def main():
	root = Tk()
	root.title("Sample Banking GUI")	
	root.geometry("300x100+100+100")

	B1 = Button(root,text = "Welcome to Tkinter bank of Python !!",fg = "#ffffff",bg = "#f69602",width = 35,padx = 20,pady = 5,command = about)
	B1.place(x=5,y=0)
	
	B2 = Button(root,text = "Sign in",command = login)
	B3 = Button(root,text = "Register",command = register)
	
	B2.place(x=100,y=30)
	B3.place(x=95,y=58)
	
	root.mainloop()


main()