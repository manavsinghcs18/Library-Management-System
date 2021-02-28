class Library:

    def __init__(self,ListOfBooks):
        self.books=ListOfBooks
    
    def DisplayAvailableBooks(self):
        print("The books present in the library are: ")
        for book in self.books:
            print(" *"+book)
    
    def BorrowBook(self,BookName):
        
        if BookName in self.books:
            print(f"You have been issued {BookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(BookName)
            return True
        else:
            print("Sorry, This book is either not available or has already isseued to someonr else, Please wait untill the book is available.")
            return False
    
    def ReturnBook(self,BookName):
        self.books.append(BookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:
    
    def RequestBook(self):
        self.book=input("Enter the name of the book you want to borrow: ")
        return self.book
    
    def ReturnBook(self):
        self.book=input("Enter the name of the book you want to return: ")
        return self.book



if __name__ == "__main__":
    CentralLibrary=Library(["Algorithm","Django","Clrs","Python Notes"])
    student=Student()
    #CentralLibrary.DisplayAvailableBooks()
    while (True):
        WelcomeMSG='''
    =====Welcome to central library=====
        Please choose the option:
        1. Listing all books.
        2. Requesting a book.
        3. Add or Return a book.
        4. Exit the library.  
        '''
        print(WelcomeMSG)

        a = int(input("Enter a choice: "))
        if a==1:
            CentralLibrary.DisplayAvailableBooks()
        elif a==2:
            CentralLibrary.BorrowBook(student.RequestBook())
        elif a==3:
            CentralLibrary.ReturnBook(student.ReturnBook())
        elif a==4:
            print("Thanks for choosing central library! Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
        
        