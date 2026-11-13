
# Library Management System

## 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is an abstract class because it defines common properties and methods that all library items should have. The late_fee() method is declared abstract because every item type has a different late fee calculation. If DVD does not implement late_fee(), Python raises a TypeError when we try to create a DVD object.

## 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

When we try to access item.__available outside the class, Python raises an AttributeError because the attribute uses double underscore name mangling. We use is_available() instead because it provides a controlled way to read the item's availability without directly accessing its internal variable. This is an example of encapsulation.

## 3. What is the difference between LibraryItem.total_items and self.title?

LibraryItem.total_items is a class attribute shared by all objects of the LibraryItem class and its child classes. It maintains the total number of items created. On the other hand, self.title is an instance attribute, meaning every object has its own title value.
