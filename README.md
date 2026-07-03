# 📚 Library Management System

A comprehensive **Object-Oriented Programming (OOP)** project built in Python that simulates a fully functional library management system. This project demonstrates advanced Python concepts including inheritance, abstraction, encapsulation, type hints, property decorators, and magic methods.

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Code Examples](#code-examples)
- [OOP Concepts Demonstrated](#oop-concepts-demonstrated)
- [Future Improvements](#future-improvements)
- [Key Skills Demonstrated](#Key-Skills-Demonstrated)
- [Author](#author)

---

## 📖 Overview

This Library Management System allows librarians and members to manage library resources efficiently. It supports:
- Adding and removing books and DVDs
- Borrowing and returning items
- Tracking due dates and overdue items
- Maintaining checkout history
- Managing users (Members and Librarians)

The project is built entirely with Python and follows **clean code principles**, making it a strong addition to my AI Engineering portfolio.

---

## ✨ Features

| **Feature** | **Description** |
| :--- | :--- |
| **Item Management** | Add, remove, and search for books and DVDs |
| **Borrowing System** | Check out and return items with due date tracking |
| **User Roles** | Members (max 5 items) and Librarians (max 10 items + admin privileges) |
| **Overdue Detection** | Automatically identifies overdue items |
| **Checkout History** | Tracks who borrowed what and when |
| **Transaction Logging** | Logs all actions for auditing |
| **Abstract Base Classes** | Enforces consistent implementation across item types |
| **Type Hints** | Self-documenting, type-safe code |
| **Magic Methods** | Pythonic object behavior (`__str__`, `__len__`, `__eq__`, etc.) |

---

## 🛠️ Technologies Used

| **Technology** | **Purpose** |
| :--- | :--- |
| **Python 3.8+** | Core programming language |
| **ABC (Abstract Base Classes)** | Define interfaces for library items and users |
| **Datetime** | Manage due dates and overdue calculations |
| **Typing** | Type hints for better code readability and IDE support |
| **No external dependencies** | Pure Python—runs anywhere |

---

## 📁 Project Structure

-library_management/  
-│  
-├── library_item.py # Defines `LibraryItem` (ABC) with abstract methods, plus `Book` and `DVD` concrete classes.  
-├── library.py # Defines the `Library` class that manages items, users, and transactions.  
-├── main.py # Demonstrates all features with sample data and outputs.  
-├── README.md # Project documentation (this file)  
-├── user.py # Defines `User` (ABC) with abstract methods, plus `Member` and `Librarian` concrete classes.

---
## 🚀 Installation

### Prerequisites
- Python 3.1 or higher installed on your system
- Git (optional, for cloning the repository)

### Steps

1. **Clone the repository**
   -git clone https://github.com/Ajtech27/library-management-system.git
   -cd library-management-system

3. **Run the program**
   python main.py

5. **Explore the code**
    -Open the files in VS Code or any Python IDE
    -Experiment with the main.py script

---
## 💻 Usage

```
Quick Start

from library_item import Book
from user import Member
from library import Library

### Create library
library = Library("Community Central")

### Add a book
book = Book("Clean Code", "Robert Martin", "B001", "978-0132350884", 464, "Programming")
library.add_item(book)

### Register a member
member = Member("Joseph", "M001", "joseph@email.com")
library.register_user(member)

### Borrow the book
member.borrow_item(book)
print(book) # Shows checked out with due date
```
---
Example Output

```
==================================================
Community Central Library | 3 items | 2 users
==================================================

Available items:
  📚 Book: The Pragmatic Programmer by Andrew Hunt [Available] | ISBN: 978-0201616224 | 352 pages | Technology
  📚 Book: Clean Code by Robert C. Martin [Available] | ISBN: 978-0132350884 | 464 pages | Programming
  🎬 DVD: Inception by Christopher Nolan [Available] | Director: Christopher Nolan | 148 min | Rating: PG-13

[Member Action]
'The Pragmatic Programmer' checked out to M001. Due: 2026-07-16

[Librarian Action]
Added 'Deep Learning' to the library.

Library now has 4 items.
```

---
## 🧠 OOP Concepts Demonstrated

Concept Implementation File  
Abstraction LibraryItem and User as Abstract Base Classes library_item.py, user.py  
Inheritance Book and DVD inherit from LibraryItem; Member and Librarian inherit from User library_item.py, user.py  
Polymorphism get_item_type() and get_loan_period() behave differently per subclass library_item.py  
Encapsulation _items, _users, _transaction_log with controlled access library.py  
Property Decorators @property, @due_date.setter for controlled attribute access library_item.py  
Type Hints : str, -> List[Book], Optional[LibraryItem] All files  
Magic Methods __str__, __repr__, __len__, __eq__, __hash__, __contains__, __getitem__ library_item.py, library.py

---

## 🔮 Future Improvements

· Data Persistence: Save library state to JSON or SQLite  
· Fine Calculation: Automatically calculate and apply fines for overdue items  
· Unit Tests: Add comprehensive test coverage with pytest  
· Web Interface: Build a simple Flask or FastAPI frontend  
· Email Notifications: Send due date reminders to members  
· Reservation System: Allow members to reserve items that are checked out  
· Reporting: Generate reports on popular items, member activity, etc.

---

## 📊 Key Skills Demonstrated
    
Object-Oriented Programming Complete OOP architecture with inheritance, abstraction, and polymorphism  
Clean Code Type hints, meaningful variable names, modular structure  
Problem Solving Complex business logic (borrowing, returns, overdue detection)  
Documentation This README, inline comments, and docstrings  
Version Control Git-friendly structure

---

## 🙏 Acknowledgments

· Built as part of my journey from Data Analysis → AI Engineering

---

## 👨‍💻 Author

Joseph Afolayan  
· 📧 ajtech012@gmail.com  
· Twitter/X: @ajtech27  
· LinkedIn: linkedin.com/in/afolayan-joseph



