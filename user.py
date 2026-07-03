from abc import ABC, abstractmethod
from typing import List
from library_item import LibraryItem


class User(ABC):
    "Abstract base class for all users in the system."
    def __init__(self, name: str, user_id: str, email: str):
        self.name = name
        self.user_id = user_id
        self.email = email
        self._borrowed_items: List[LibraryItem] = []

    @property
    def borrowed_items(self) -> List[LibraryItem]:
        """Return a list of items currently borrowed by the user."""
        return self._borrowed_items()
    
    @property
    def borrowed_count(self) -> int:
        """Return the number of items currently borrowed by the user."""
        return len(self._borrowed_items)
    
    def borrow_item(self, item: LibraryItem) -> str:
        """Borrow an item from the library."""
        if item.is_checked_out:
            return f"Item '{item.title}' is not available."
        if len(self._borrowed_items) >= self.get_max_loan_limit():
            return f"User '{self.name}' has reached the borrow limit."
        
        result = item.check_out(self.user_id)
        self._borrowed_items.append(item)
        return result
    
    @abstractmethod
    def get_max_loan_limit(self) -> int:
        """Return the maximum number of items the user can borrow."""
        pass

    def __str__(self) -> str:
        """Return a string representation of the user."""
        return f"{self.__class__.__name__}: {self.name} (ID: {self.user_id})"  

class Member(User):
    """Concrete class representing regular library member."""
    def get_max_loan_limit(self) -> int:
        """Return the maximum number of items a member can borrow."""
        return 5  # Members can borrow up to 5 items

class Librarian(User):
    """Librarian with extended privileges."""
    def __init__(self, name: str, user_id: str, email: str, department: str = "General"):
        super().__init__(name, user_id, email)
        self.department = department

    def get_max_loan_limit(self) -> int:
        """Return the maximum number of items a librarian can borrow."""
        return 10  # Librarians can borrow up to 10 items
    
    def add_item(self, library, item: 'LibraryItem') -> str:
        """Add a new item to the library."""
        library.add_item(item)
        return f"Added '{item.title}' to the library by librarian '{self.name}'."
    
    def remove_item(self, library, item_id: str) -> str:
        """Remove an item from the library."""
        if library.remove_item(item_id):
            return f"Item {item_id} removed successfully by librarian '{self.name}'."
        return f"Item {item_id} not found."