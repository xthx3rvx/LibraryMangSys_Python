from abc import ABC, abstractmethod
from datetime import datetime

class LibraryDepartment(ABC):
    @abstractmethod
    def manageSection(self):
        pass

class ScienceSection(LibraryDepartment):
    def manageSection(self):
        print("Managing Science Section: Physics, Chemistry, Biology books.")

class ArtsSection(LibraryDepartment):
    def manageSection(self):
        print("Managing Arts Section: Literature, History, Philosophy books.")

class Member:
    def __init__(self, memberID, name, contact):
        self.memberID = memberID
        self.name = name
        self.contact = contact

    def displayMemberDetails(self):
        print(f"Member ID: {self.memberID}, Name: {self.name}, Contact: {self.contact}")

class StudentMember(Member):
    def __init__(self, memberID, name, contact, collegeName):
        super().__init__(memberID, name, contact)
        self.collegeName = collegeName

    def displayMemberDetails(self):  # Run-Time Polymorphism
        super().displayMemberDetails()
        print(f"College: {self.collegeName}")

class FacultyMember(Member):
    def __init__(self, memberID, name, contact, department):
        super().__init__(memberID, name, contact)
        self.department = department

    def displayMemberDetails(self):  # Run-Time Polymorphism
        super().displayMemberDetails()
        print(f"Department: {self.department}")

class Transaction:
    def __init__(self, bookID, issueDate, returnDate):
        self.__bookID = bookID
        self.__issueDate = issueDate
        self.__returnDate = returnDate

    def getBookID(self):
        return self.__bookID

    def getIssueDate(self):
        return self.__issueDate

    def getReturnDate(self):
        return self.__returnDate

    def setBookID(self, bookID):
        self.__bookID = bookID

    def setIssueDate(self, issueDate):
        self.__issueDate = issueDate

    def setReturnDate(self, returnDate):
        self.__returnDate = returnDate

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def displayBook(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}")

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def addBook(self, book):
        self.books.append(book)

    def addMember(self, member):
        self.members.append(member)

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def showBooks(self):
        print("\nLibrary Books:")
        for book in self.books:
            book.displayBook()

    def showMembers(self):
        print("\nLibrary Members:")
        for member in self.members:
            member.displayMemberDetails()

    def showTransactions(self):
        print("\nLibrary Transactions:")
        for t in self.transactions:
            print(f"BookID: {t.getBookID()}, Issue: {t.getIssueDate().date()}, Return: {t.getReturnDate().date()}")

def calculateFine(member, daysLate):
    if isinstance(member, StudentMember):
        return 15 * daysLate 
    elif isinstance(member, FacultyMember):
        return 5 * daysLate 
    else:
        return 10 * daysLate 

if __name__ == "__main__":
   
    lib = Library()

    lib.addBook(Book("The Alchemist", "Paulo Coelho", "9780061122415"))
    lib.addBook(Book("A Brief History of Time", "Stephen Hawking", "9780553380163"))

    s1 = StudentMember(1, "Atharva", "9876XXXXXX", "XYZ College")
    f1 = FacultyMember(2, "Dr. Sharma", "9123XXXXXX", "Physics")
    lib.addMember(s1)
    lib.addMember(f1)

    t1 = Transaction("9780061122415", datetime(2025, 6, 1), datetime(2025, 6, 15))
    lib.addTransaction(t1)

    lib.showBooks()
    lib.showMembers()
    lib.showTransactions()

    print("\nLibrary Departments:")
    sci = ScienceSection()
    art = ArtsSection()
    sci.manageSection()
    art.manageSection()

    daysLate = 3
    print(f"\nFine for {s1.name} (Student, {daysLate} days late): Rs.{calculateFine(s1, daysLate)}")
    print(f"Fine for {f1.name} (Faculty, {daysLate} days late): Rs.{calculateFine(f1, daysLate)}")
