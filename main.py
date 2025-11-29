# ===========================================
#  Library Book Management System
#  Using Singly Linked List and Stack
# ===========================================
class BookNode:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None


# Singly Linked List to manage books
class BookList:
    def __init__(self):
        self.head = None

    # Insert a new book at the end
    def insertBook(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if self.head is None:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print(f"✅ Book '{title}' added successfully.")

    # Delete book by ID
    def deleteBook(self, book_id):
        temp = self.head
        prev = None
        while temp and temp.book_id != book_id:
            prev = temp
            temp = temp.next
        if not temp:
            print("⚠️ Book not found!")
            return False
        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next
        print(f"🗑️ Book '{temp.title}' deleted successfully.")
        return True

    # Search book by ID
    def searchBook(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                print(f"\n📘 Book Found:\nID: {temp.book_id}\nTitle: {temp.title}\nAuthor: {temp.author}\nStatus: {temp.status}")
                return temp
            temp = temp.next
        print("⚠️ Book not found!")
        return None

    # Display all books
    def displayBooks(self):
        if not self.head:
            print("📚 Library is empty.")
            return
        temp = self.head
        print("\n📚 Current Books in Library:")
        print("-" * 40)
        while temp:
            print(f"ID: {temp.book_id} | Title: {temp.title} | Author: {temp.author} | Status: {temp.status}")
            temp = temp.next
        print("-" * 40)


# Stack class for undo mechanism
class TransactionStack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("⚠️ No transaction to undo.")
            return None

    def isEmpty(self):
        return len(self.stack) == 0

    def viewTransactions(self):
        if not self.stack:
            print("🕒 No transactions yet.")
        else:
            print("\n📜 Recent Transactions:")
            for i, t in enumerate(reversed(self.stack), 1):
                print(f"{i}. {t}")


# Transaction Management
class LibrarySystem:
    def __init__(self):
        self.book_list = BookList()
        self.transactions = TransactionStack()

    def issueBook(self, book_id):
        book = self.book_list.searchBook(book_id)
        if book and book.status == "Available":
            book.status = "Issued"
            self.transactions.push(("issue", book_id))
            print(f"📕 Book '{book.title}' has been issued.")
        elif book:
            print("⚠️ Book already issued.")

    def returnBook(self, book_id):
        book = self.book_list.searchBook(book_id)
        if book and book.status == "Issued":
            book.status = "Available"
            self.transactions.push(("return", book_id))
            print(f"📗 Book '{book.title}' has been returned.")
        elif book:
            print("⚠️ Book is not issued.")

    def undoTransaction(self):
        last = self.transactions.pop()
        if not last:
            return
        action, book_id = last
        book = self.book_list.searchBook(book_id)
        if action == "issue":
            book.status = "Available"
            print(f"↩️ Undo: Book '{book.title}' is now Available again.")
        elif action == "return":
            book.status = "Issued"
            print(f"↩️ Undo: Book '{book.title}' is marked as Issued again.")
if __name__ == "__main__":
    system = LibrarySystem()
    system.book_list.insertBook(101, "Python Basics", "Utsav Ratan")
    system.book_list.insertBook(102, "Data Structures", "Utsav Ratan")
    system.book_list.displayBooks()

    system.issueBook(101)
    system.returnBook(101)
    system.undoTransaction()
    system.book_list.displayBooks()
    system.transactions.viewTransactions()