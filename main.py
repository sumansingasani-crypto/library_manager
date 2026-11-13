
# main.py

from models import Book, Magazine, DVD, Member, LibraryItem


# 1. Create library items

book = Book("Python 101", 1, "A. Rao")

magazine = Magazine("Science Today", 2, 101)

dvd = DVD("Python Movie", 3, 120)

extra_book = Book("Data Structures", 4, "B. Kumar")


# 2. Create members

alice = Member("Alice", 101)

bob = Member("Bob", 102, max_items=1)


print("========== LIBRARY MANAGEMENT SYSTEM ==========")


# 3. Borrowing an item

try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())

except ValueError as e:
    print("Could not borrow:", e)


# 4. Try borrowing an already borrowed item

try:
    bob.borrow(book)

except ValueError as e:
    print("Could not borrow:", e)


# 5. Alice borrows remaining items

try:
    alice.borrow(magazine)
    print("Alice borrowed:", magazine.describe())

    alice.borrow(dvd)
    print("Alice borrowed:", dvd.describe())

except ValueError as e:
    print("Could not borrow:", e)


# 6. Trigger borrowing limit error

try:
    alice.borrow(extra_book)

except ValueError as e:
    print("Could not borrow:", e)


# 7. Try returning an item not borrowed by Bob

try:
    bob.return_item(book)

except ValueError as e:
    print("Could not return:", e)


# 8. Polymorphism - Late fee calculation

print("\n========== LATE FEE CALCULATION ==========")

items = [book, magazine, dvd]

for item in items:

    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )


# 9. Return a borrowed item

print("\n========== RETURN ITEM ==========")

try:
    fee = alice.return_item(book, days_late=3)

    print("Alice returned:", book.title)
    print("Late fee: Rs", fee)

except ValueError as e:
    print("Could not return:", e)


# 10. Check borrowed items

print("\n========== MEMBER BORROWED ITEMS ==========")

print("Alice's borrowed items:", alice.borrowed_titles())


# 11. Check availability

print("\n========== AVAILABILITY CHECK ==========")

print("Book available:", book.is_available())
print("Magazine available:", magazine.is_available())
print("DVD available:", dvd.is_available())


# 12. Demonstrate encapsulation

print("\n========== ENCAPSULATION ==========")

try:
    print(book.__available)

except AttributeError as e:
    print("Private attribute cannot be accessed:", type(e).__name__)

print("Correct way to check availability:", book.is_available())


# 13. Total items created

print("\n========== TOTAL ITEMS ==========")

print("Total items created:", LibraryItem.total_items)
