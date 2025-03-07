"""library management"""
def library():
    books=[]#empty list
    record={}#empty dictionary
    """a function add book to add the books to the list (books) by taking user input
    """
    def addbook():
            while True:#condition to run the loop till the condition remain right
                choice=input(" 1. To add books \n 2. To exit : ")
                if choice=="1":
                    n=int(input("entert the number of books to be entered : "))
                    for i in range(0,n):
                        name=input().title()
                        books.append(name)#adding elements or books in the list
                else:
                    print("exited successfully")
                    break
    """a function to diplay the available books if books are availabel
    where length is used to check wheter books is present in it or not
    """             
    def diplay():
            if len(books)>0:
                print("available books")
                [print(book) for book in books]
            else:
                 print("not availabel") 
    """function to issue the books to user"""
    def issuebook():
        name=input("please enter name : ").title()
        print(f"hello {name} ")
        no=int(input("please enter how many books you want to issue : "))
        if len(books)>=no:
            print(f"enter name of {no}  books")
            value=[]#empty list to store the no of books issurd by a user
            for i in range(0,no):
                bname=input().title()
                if bname in books:
                    value.append(bname)#list to store the books issued by the user
                    books.remove(bname)
                else:
                    print("book not available in library")
        record[name]=value# inserting the list of books that user have taken
        print(f"{name} has issue the books ",record[name])
    """function to return the books"""
    def bookreturn():
        name=input("enter yor name : ").title()
        if name in record:
            print(f"{name} you have issued these books ",record[name])
            n=int(input("enter the number of books you want to return : "))
            for i in range(0,n):
                bname=input().title()
                if bname in record[name]:
                    books.append(bname)
                    record[name].remove(bname)
            print("successful")
        else:
            print(f"user {name} doesnot exist")
    def searchbooks():
        bname=input("enter the name of books to be serched : ").title()
        for i in record.values():
            print("already issued" if bname in i else "it is avilable" if bname in books else "not available")
         
    while True:
            print("\nLibrary Management System : ")
            print("1. Add Book")
            print("2. Display Books")
            print("3. To issue item")
            print("4.To return the book")
            print("5.To search the books")
            print("6. Exit")
            ch= input("Enter choice : ")
            if ch == "1":
                addbook()
            elif ch == "2":
                diplay()
            elif ch=="3":
                 issuebook()
            elif ch=="4":
                bookreturn()
            elif ch=="5":
                searchbooks()
            elif ch=="6":
                print("Exiting the system.")
                break
                  
            else:
                  print("Invalid choice, please try again.")
auth={"manish":"12345"}#dictionary containing the name and password of permanent admin
while True:
    n=input("enetr name : ")
    no=input("enter pass : ")
    if n in auth and no==auth[n]:
        print("1.Press1 to add new admin\n2.To exit ")
        admin=input()
        if admin=="1":
             name=input("enter name : ")
             password=input("enert the password : ")
             auth[name]=password #adding new admin for the library
             print("successfull : ",auth)
             library()
             break
        else:
             library()
             break
    else:
         print("incorrect user name and password")
     
    