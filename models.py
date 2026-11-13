
# models.py

from abc import ABC, abstractmethod


# 1. Abstract Parent Class
class LibraryItem(ABC):

    total_items = 0

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

        self.__available = True

        LibraryItem.total_items += 1

    def is_available(self):
        return self.__available

    def mark_borrowed(self):
        self.__available = False

    def mark_returned(self):
        self.__available = True

    @abstractmethod
    def late_fee(self, days_late):
        pass


# 2. Book Child Class
class Book(LibraryItem):

    DAILY_RATE = 2

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"


# 3. Magazine Child Class
class Magazine(LibraryItem):

    DAILY_RATE = 1

    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Magazine: {self.title}, Issue {self.issue_number} (ID {self.item_id})"


# 4. DVD Child Class
class DVD(LibraryItem):

    DAILY_RATE = 5

    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"DVD: {self.title}, Duration {self.duration_minutes} minutes (ID {self.item_id})"


# 5. Member Class
class Member:

    def __init__(self, name, member_id, max_items=3):

        self.name = name
        self.member_id = member_id
        self.max_items = max_items

        self.__borrowed = []

    def borrow(self, item):

        # Check item availability
        if not item.is_available():
            raise ValueError(f"'{item.title}' is already borrowed.")

        # Check borrowing limit
        if len(self.__borrowed) >= self.max_items:
            raise ValueError(
                f"{self.name} has reached borrowing limit ({self.max_items} items)."
            )

        # Update item availability
        item.mark_borrowed()

        # Add item to member's borrowed list
        self.__borrowed.append(item)

    def return_item(self, item, days_late=0):

        # Check whether member has borrowed this item
        if item not in self.__borrowed:
            raise ValueError(
                f"{self.name} has not borrowed '{item.title}'."
            )

        # Mark item as available
        item.mark_returned()

        # Remove item from borrowed list
        self.__borrowed.remove(item)

        # Calculate and return late fee
        return item.late_fee(days_late)

    def borrowed_titles(self):

        return [item.title for item in self.__borrowed]
