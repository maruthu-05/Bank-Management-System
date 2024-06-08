#Online ATM
import mysql.connector
print('''-------------BANK MANAGEMENT SYSTEM---------------
+ ^^^^^^^^^^^^^ ORGANISED BY- ^^^^^^^^^^^^^^^^^^^+
+                                                +
+ $$$         1)S.V.MARUTHAVANAN             $$$ +
+                                                +
----------!!!THANKS FOR CHOOSING US!!!------------
''')
print('''
''')
usern=input("Enter your MySQL username:")
passw=input("Enter your MySQL password:")
my=mysql.connector.connect(host="localhost",user=usern,passwd=passw,database="eatm")
mycursor=my.cursor()

def addacc():
    user=input("User name:")
    acc=input("Enter account number:")
    dat=input("Enter the account created date(DD/MM/YYYY)(type with/):")
    cn=str(input("Enter the contact number:"))
    mycursor.execute("insert into atm values('"+user+"'"+',"'+acc+'","'+dat+'",'"+mon+",'"+cn+"'+");")
    print("****Detail successfully added****")

                 
def withdraw():
    ac=input("Enter the account number:")
    amount=int(input("PLEASE ENTER AMOUNT TOWITHDRAW : "))
    sql='UPDATE atm SET money = money- %s'
    mycursor.execute(sql ,(amount,))
    mycursor.execute("COMMIT")
    print("#**#Rup",amount,"is successfully withdrawed#**#")

def alldet():
    a=mycursor.execute("select * from atm")
    fet=mycursor.fetchall()
    for row in fet:
        print(row)
        print('''
        ''')

def cusdet():
    accno=input("Enter the account number:")
    mycursor.execute("select * from atm where accno="+accno)
    fet=mycursor.fetchall()
    for row in fet:
        print(row)

def add():
    accno=input("Enter the account number:")
    mycursor.execute("select dateofcreation from atm where accno="+accno)
    fet=mycursor.fetchall()
    for row in fet:
        print(row)

def con():
    accno=input("Enter the account number:")
    mycursor.execute("select cno from atm where accno="+accno)
    fet=mycursor.fetchall()
    for row in fet:
        print(row)

def us():
    accno=input("Enter the account number:")
    mycursor.execute("select user from atm where accno="+accno)
    fet=mycursor.fetchall()
    for row in fet:
        print(row)

def bal():
    accno=input("Enter the account number:")
    mycursor.execute("select money from atm where accno="+accno)
    fet=mycursor.fetchall()
    for row in fet:
        print(row)

print("""************MODE OF CHOICES************
* 1 for Add new customer *
* 2 for Showing all the customer *
* 3 for Withdraw money *
* 4 for Show the customer detail *
* 5 for Show date of creation by accno *
* 6 for Show phone number by accno *
* 7 for Show user name by accno *
* 8 for Show balance in the acc *
* 9 for Exit *
***************************************""")
y=True
while y==True:
        print('''
        ''')
        c=int(input("Enter your choice:"))
        if c==1:
         mon=input("Enter your deposit amount:")
         addacc()
        elif c==2:
         alldet()
        elif c==3:
         withdraw()
        elif c==4:
         cusdet()
        elif c==5:
         add()
        elif c==6:
         con()
        elif c==7:
         us()
        elif c==8:
         bal()
        elif c==9:
         break
