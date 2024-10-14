import datetime
with open("Booklist.txt",'r') as f:
    book_list = [line.strip() for line in f.readlines()]
class library:
    def __init__(self):
        pass
    def add_books(self):
        with open('Booklist.txt','a') as f:
            book_name = input("Enter the book name: ")
            if book_name in book_list:
                print("Book already exists")
            else:
                book_list.append(book_name)
                f.write(book_name + "\n")
                print("Book added successfully")
    def borrow_book(self):
        book_name= input("Enter the name of the book You want to Borrow:")
        if book_name in book_list:
            print("The Book is Available and You can Borrow it")
            book_list.remove(book_name)
            with open("Booklist.txt",'w') as f :
                for i in book_list:
                    f.write(i + "\n")
        else:
            print("Sorry! The book is not available and You can not Borrow it")
    def return_book(self):
        book_name= input("Enter the name of the book You want to return:")
        if book_name not in book_list:
            date = input("Enter the date of borrow (year-month-date):-")
            borrow_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            current_date =datetime.date.today()
            difference = current_date - borrow_date
            if difference >= datetime.timedelta(days=30):
                fine = (difference - datetime.timedelta(days=30)).days * 10
                print(f"You have to pay a fine of {fine} as You have not returend the book in time")
            print("The Book is not Available and You can return it along with the fine")
            book_list.append(book_name)
            with open('Booklist.txt', 'w') as f:
                for i in book_list:
                    f.write(i + "\n")
            print("Book Added successfully")
        else:
            print("Sorry! The book is available and You can not return it")
    def check(self):
        book_name = input("Enter the name of the book You wantto check:")
        if book_name in book_list:
            print("The Book is Available")
        else:
            print("Sorry! The book is not available")
print("Welcome to XYZ Library")
print("1 to add book")
print("2 to borrow book")
print("3 to return anybook")
print("4 to check any book available or not")
a = int(input("Enter Your choice:-"))
match a :
    case 1 :
        l = library()
        l.add_books()
    case 2 :
        l = library()
        l.borrow_book()
    case 3 :
        l = library()
        l.return_book()
    case 4 :
        l = library()
        l.check()
    case _ :
        raise ValueError("You have entered a invalid Option")