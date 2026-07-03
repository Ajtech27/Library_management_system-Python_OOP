from library_item import LibraryItem, Book, DVD
from library import Library
from user import Member, Librarian
from datetime import datetime, timedelta

def main():
    library = Library("City Library")

    book1 = Book(title = "The Pragmatic Programmer", 
                 author = "Andrew Hunt and David Thomas",
                 item_id= "B001",
                 isbn = "978-0201616224",
                 pages = 352,
                 genre= "Technology"
                 )
    
    book2 = Book(title= "Rich Dad Poor Dad",
                 author= "Robert T. Kiyosaki",
                 item_id= "B002",
                 isbn= "978-1612680194",
                 pages= 336,
                 genre= "Finance" 
                 )
    
    book3 = Book(title= "The Lean Startup",
                 author= "Eric Ries",
                 item_id= "B003",
                 isbn= "978-0307887704",
                 pages= 320,
                 genre= "Entrepreneurship"
                 )
    
    dvd1 = DVD(title= "The Shawshank Redemption",
                author= "Frank Darabont",
                item_id= "D001",
                director= "Frank Darabont",
                duration= 142,
                rating= "R"
                )
    
    dvd2 = DVD(title= "Inception",
                author= "Christopher Nolan",
                item_id= "D002",
                director= "Christopher Nolan",
                duration= 148,
                rating= "PG-13"
                )
    
    #Add item to library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    library.add_item(dvd1)
    library.add_item(dvd2)

    #Register users
    member = Member(name= "Joseph Richard", 
                     user_id= "M001",
                     email= "josephrich@email.com")
    member2 = Member(name= "Emily Clark",
                     user_id= "M002",
                     email= "emilycla@email.com")
    
    librarian = Librarian(name= "Sarah Johnson",
                            user_id= "L001",
                            email= "sarahjohn@citylib.com",
                            department= "IT"
                            )
    
    library.register_user(member)
    library.register_user(member2)
    library.register_user(librarian)
    
    print("=" * 50)
    print(library)
    print("=" * 50)
    
    # Show available items
    print("\nAvailable items:")
    for item in library.get_available_items():
        print(f"  {item}")
    
    print("\n" + "=" * 50)
    
    # Member borrows a book
    print("\n[Member Action]")
    print("\n *A member borrows a Book")
    print(member.borrow_item(book1))
    
    # Try to borrow same book again
    print("\n *trying to borrow the same book again")
    print(member.borrow_item(book1))
    
    # Show item status
    print("\n *Status of the borrowed book")
    print(f"\n{book1}")
    print(f"Is '{book1.title}' overdue? {book1.is_overdue()}")
    
    print("\n" + "=" * 50)
    
    # Librarian adds an item
    print("\n[Librarian Action]")
    print("\n *A librarian adds a new book")
    new_book = Book(
        title="Deep Learning",
        author="Ian Goodfellow",
        item_id="B003",
        isbn="978-0262035613",
        pages=800,
        genre="AI"
    )
    print(librarian.add_item(library, new_book))
    
    print(f"\nLibrary now has {len(library)} items.")
    
    print("\n" + "=" * 50)
    
    # Using magic methods
    print("\n[Magic Methods Demo]")
    print(f"Book title length: {len(book1)} characters")
    print(f"Book1 == Book2? {book1 == book2}")
    print(f"Is book1 in library? {book1 in library}")
    print(f"Library['B001']: {library['B001']}")
    
    print("\n" + "=" * 50)
    
    # Check transaction log
    print("\n[Transaction Log]")
    for log in library.get_transaction_log():
        print(f"  {log}")

if __name__ == "__main__":
    main()


                           
                    



