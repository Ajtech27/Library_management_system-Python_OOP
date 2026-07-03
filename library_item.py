from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Optional,Tuple

class LibraryItem(ABC):
    """Abstract base class for all library items."""

    def __init__(self, title: str, author: str, item_id: str):
        self.title = title
        self.author = author
        self.item_id = item_id
        self._is_checked_out = False
        self._checked_out_by: Optional[str] = None
        self._due_date: Optional[datetime] = None
        self._checkout_history: List[Tuple[str, datetime]] = []

    @property
    def is_checked_out(self) -> bool:
        """Check if the item is currently checked out."""
        return self._is_checked_out
    
    @property
    def due_date(self) -> Optional[datetime]:
        """Get the due date of the item."""
        return self._due_date
    
    @due_date.setter
    def due_date(self, days: Optional[int]) -> None:
        if days is None:
            self._due_date = None
        elif days <= 0:
            raise ValueError("Due date must be at least 1 day.")
        else:
            self._due_date = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        ) + timedelta(days=days)

    @abstractmethod
    def get_item_type(self) -> str:
        """Return the type of the library item."""
        pass

    @abstractmethod
    def get_loan_period(self) -> int:
        """Return the loan period in days for the item."""
        pass

    def check_out(self, member_id: str) -> str:
        """Check out the item to a library member."""
        if self._is_checked_out:
            return f"Item '{self.title}' is already checked out."
        self._is_checked_out = True
        self._checked_out_by = member_id
        self.due_date = self.get_loan_period() 
        #self.due_date = datetime.now() + timedelta(days=self.get_loan_period())
        self._checkout_history.append((member_id, datetime.now()))
        return f"Item '{self.title}' checked out by member '{member_id}'. Due date: {self.due_date.strftime('%Y-%m-%d')}"
    
    def return_item(self) -> str:
        """Return the item to the library."""
        if not self._is_checked_out:
            return f"Item '{self.title}' is not checked out."
        self._is_checked_out = False
        self._checked_out_by = None
        self._due_date = None
        return f"Item '{self.title}' has been returned successfully."

    def is_overdue(self) -> bool:
        """Check if the item is overdue."""
        if not self._is_checked_out or self.due_date is None:
            return False
        return datetime.now() > self.due_date
    
    def get_checkout_history(self) -> List[Tuple[str, datetime]]:
        """Return the checkout history of the item."""
        return self._checkout_history.copy()
    
    def __str__(self):
        """Return a string representation of the library item."""
        status = "Available" if not self._is_checked_out else f"Checked out (due: {self._due_date.strftime('%Y-%m-%d') if self.due_date else 'Unknown'}) {self._checked_out_by}, due on {self.due_date.strftime('%Y-%m-%d') if self.due_date else 'N/A'})"
        return f"{self.get_item_type()}: {self.title} by {self.author}[{status}]"
    
    def __repr__(self) -> str:
        """Representation of the library item for debugging."""
        return f"{self.__class__.__name__}(title='{self.title}', author={self.author}, item_id={self.item_id}, is_checked_out={self._is_checked_out}, checked_out_by={self._checked_out_by!r}, due_date={self.due_date!r})"
     
    def __eq__(self, other: object) -> bool:
        """Check equality based on item_id."""
        if not isinstance(other, LibraryItem):
            return False
        return self.item_id == other.item_id
        
    def __len__(self) -> int:
        """Return the length of the title."""
        return len(self.title)
    
    def __hash__(self) -> int:
        """Return a hash based on the item_id."""
        return hash(self.item_id)


class Book(LibraryItem):
    """Concrete class representing a book in the library."""

    def __init__(self, title: str, author: str, item_id: str, isbn: str, pages: int, genre: str):
        super().__init__(title, author, item_id)
        self.isbn = isbn
        self.pages = pages
        self.genre = genre
    
    def get_item_type(self) -> str:
        """Return the type of the library item."""
        return "Book"
    
    def get_loan_period(self) -> int:
        """Return the loan period in days for a book."""
        return 14  # Books can be borrowed for 14 days
    
    def __str__(self) -> str:
        """Return a string representation of the book."""
        return f"{super().__str__()} | ISBN: {self.isbn} | Pages: {self.pages} | Genre: {self.genre}"

class DVD(LibraryItem):
    """Concrete class representing a DVD in the library."""

    def __init__(self, title: str, author: str, item_id: str, director: str, duration: int, rating: str):
        super().__init__(title, author, item_id)
        self.director = director
        self.duration = duration  # Duration in minutes
        self.rating = rating
    
    def get_item_type(self) -> str:
        """Return the type of the library item."""
        return "DVD"
    
    def get_loan_period(self) -> int:
        """Return the loan period in days for a DVD."""
        return 7  # DVDs can be borrowed for 7 days
    
    def __str__(self) -> str:
        """Return a string representation of the DVD."""
        return f"{super().__str__()} | Director: {self.director} | Duration: {self.duration} mins | Rating: {self.rating}"