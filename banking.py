import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(host="localhost", user="root", password="Rohan@1997", database="rohan")
mycursor=mydb.cursor()


def script():

    def acc_insert():

        l = []
        accno = input("Enter the Account number : ")
        l.append(accno)
        name = input("Enter the Customer Name: ")
        l.append(name)
        age = input("Enter Age of Customer : ")
        l.append(age)
        unqc = input("Enter the Unique Code : ")
        l.append(unqc)

        tup = (l)
        sql = "Insert into bank(Acc_No,Name,Age,Unique_Code) values(%s,%s,%s, %s)"
        mycursor.execute(sql, tup)
        mydb.commit()

    def acc_view():

        print("Select the search criteria : ")
        print("1. Acc no")
        print("2. Name")
        print("3. Age")
        print("4. Unique Code")

        ch = int(input("Enter the choice : "))
        if ch == 1:
            s = input("Enter ACC no : ")
            rl = (s,)
            sql = "select * from bank where Acc_No=%s"
            mycursor.execute(sql, rl)
        elif ch == 2:
            s = input("Enter Name : ")
            rl = (s,)
            sql = "select * from bank where Name=%s"
            mycursor.execute(sql, rl)
        elif ch == 3:
            s = input("Enter Age : ")
            rl = (s,)
            sql = "select * from bank where Age=%s"
            mycursor.execute(sql, rl)

        elif ch == 4:
            s = input("Enter Unique Code : ")
            rl = (s,)
            sql = "select * from bank where Unique_Code=%s"
            mycursor.execute(sql, rl)

        res = mycursor.fetchall()
        print("The Account details are as follows : ")
        k = pd.DataFrame(res, columns=['AcNo', 'Name', 'Age', 'Unique_Code'])
        print(k)

    def close_acc():

        Accno=input("Enter the Account number of the Customer to be closed : ")
        rl=(Accno,)
        sql="Delete from bank where Acc_No=%s"
        mycursor.execute(sql,rl)
        mydb.commit()

    def bank_menu():

        print("Enter 1 : To Add Customer")
        print("Enter 2 : To View Customer ")
        print("Enter 3 : To Close Account")

        try:
            userInput = int(input("Please Select An Above Option: "))
        except ValueError:
            exit("\nEnter a Number")
        else:
            print("\n")
            if(userInput == 1):
                acc_insert()
            elif (userInput==2):
                acc_view()
            elif (userInput==3):
                close_acc()
            else:
                print("Enter correct choice. . . ")

    bank_menu()
    restart = input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("Programme terminating. Goodbye.")


script()
