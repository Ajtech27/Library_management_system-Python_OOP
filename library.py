from typing import Dict, List, Optional, Set
from datetime import datetime, timedelta
from library_item import LibraryItem
from user import User

class Library:
    """Main library management system."""
    
    def __init__(self, name: str):
        self.name = name
        self._items: Dict[str, LibraryItem] = {}  # item_id -> LibraryItem
        self._users: Dict[str, User] = {}         # user_id -> User
        self._transaction_log: List[str] = []

    @property
    def total_items(self) -> int:
        """Property: Total items in library."""
        return len(self._items)

    @property
    def total_users(self) -> int:
        """Property: Total registered users."""
        return len(self._users)

    def add_item(self, item: LibraryItem) -> None:
        """Add an item to the library."""
        self._items[item.item_id] = item
        self._log(f"Added item: {item.title}")

    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the library."""
        if item_id in self._items:
            del self._items[item_id]
            self._log(f"Removed item: {item_id}")
            return True
        return False

    def register_user(self, user: User) -> None:
        """Register a user."""
        self._users[user.user_id] = user
        self._log(f"Registered user: {user.name}")

    def get_item(self, item_id: str) -> Optional[LibraryItem]:
        """Get an item by ID."""
        return self._items.get(item_id)

    def find_item_by_title(self, title: str) -> List[LibraryItem]:
        """Find items by title (case-insensitive partial match)."""
        title_lower = title.lower()
        return [item for item in self._items.values() 
                if title_lower in item.title.lower()]

    def get_available_items(self) -> List[LibraryItem]:
        """Get all available (not checked out) items."""
        return [item for item in self._items.values() 
                if not item.is_checked_out]

    def get_overdue_items(self) -> List[LibraryItem]:
        """Get all overdue items."""
        return [item for item in self._items.values() 
                if item.is_overdue()]

    def _log(self, message: str) -> None:
        """Add a message to transaction log."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transaction_log.append(f"[{timestamp}] {message}")

    def get_transaction_log(self) -> List[str]:
        """Get all transaction logs."""
        return self._transaction_log.copy()

    # Magic Methods
    def __str__(self) -> str:
        return f"{self.name} Library | {self.total_items} items | {self.total_users} users"

    def __len__(self) -> int:
        return self.total_items

    def __contains__(self, item: LibraryItem) -> bool:
        """Check if an item exists in the library."""
        return item.item_id in self._items

    def __getitem__(self, item_id: str) -> Optional[LibraryItem]:
        """Allow indexing: library['item_id']"""
        return self.get_item(item_id)