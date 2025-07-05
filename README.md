# LibraryMangSys_Python
📚 Library Management System (OOP-Based in Python)
This project is a simple Library Management System built using Object-Oriented Programming (OOP) principles in Python. It models a real-world library system with features like managing books, members (students and faculty), transactions, and different library departments.

🚀 Features
Book Management: Add and display books with title, author, and ISBN.

Member Management:

Supports both StudentMember and FacultyMember using inheritance and runtime polymorphism.

Displays detailed member information.

Transactions:

Handles book issue and return transactions.

Stores issue and return dates for fine calculation.

Library Departments:

Abstract class LibraryDepartment with concrete subclasses ScienceSection and ArtsSection implementing manageSection() method.

Fine Calculation:

Calculates fines based on member type and days late (Students: ₹15/day, Faculty: ₹5/day, Others: ₹10/day).

🧠 Concepts Demonstrated
Abstraction (LibraryDepartment as an abstract base class)

Inheritance (StudentMember and FacultyMember extend Member)

Encapsulation (Transaction class with private attributes and getter/setter methods)

Polymorphism (method overriding in displayMemberDetails)

Composition (Library class aggregates books, members, and transactions)

📦 Dependencies
Python 3.x

datetime module (standard in Python)

🧑‍💻 Author
-ATHARVA HANCHATE
