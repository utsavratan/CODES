#include <iostream>
#include <stack>
#include <string>
using namespace std;
class BookNode {
public:
    int bookID;
    string title;
    string author;
    string status;
    BookNode* next;

    BookNode(int id, string t, string a, string s = "Available") {
        bookID = id;
        title = t;
        author = a;
        status = s;
        next = nullptr;
    }
};

class BookList {
private:
    BookNode* head;

public:
    BookList() { head = nullptr; }

    void insertBook(int id, string title, string author) {
        BookNode* newBook = new BookNode(id, title, author);
        if (head == nullptr) {
            head = newBook;
        } else {
            BookNode* temp = head;
            while (temp->next != nullptr)
                temp = temp->next;
            temp->next = newBook;
        }
        cout << "✅ Book '" << title << "' added successfully.\n";
    }

    bool deleteBook(int id) {
        BookNode* temp = head;
        BookNode* prev = nullptr;

        while (temp != nullptr && temp->bookID != id) {
            prev = temp;
            temp = temp->next;
        }

        if (temp == nullptr) {
            cout << "⚠️ Book not found!\n";
            return false;
        }

        if (prev == nullptr)
            head = temp->next;
        else
            prev->next = temp->next;

        cout << "🗑️ Book '" << temp->title << "' deleted successfully.\n";
        delete temp;
        return true;
    }
    BookNode* searchBook(int id) {
        BookNode* temp = head;
        while (temp != nullptr) {
            if (temp->bookID == id) {
                cout << "\n📘 Book Found:\n";
                cout << "ID: " << temp->bookID << "\nTitle: " << temp->title 
                     << "\nAuthor: " << temp->author << "\nStatus: " << temp->status << "\n";
                return temp;
            }
            temp = temp->next;
        }
        cout << "⚠️ Book not found!\n";
        return nullptr;
    }

    void displayBooks() {
        if (head == nullptr) {
            cout << "📚 Library is empty.\n";
            return;
        }

        cout << "\n📚 Current Books in Library:\n";
        cout << "-----------------------------------------\n";
        BookNode* temp = head;
        while (temp != nullptr) {
            cout << "ID: " << temp->bookID << " | Title: " << temp->title
                 << " | Author: " << temp->author
                 << " | Status: " << temp->status << endl;
            temp = temp->next;
        }
        cout << "-----------------------------------------\n";
    }
};

struct Transaction {
    string type;
    int bookID;
};

class TransactionStack {
private:
    stack<Transaction> transactions;

public:
    void push(string type, int id) {
        transactions.push({type, id});
    }

    bool isEmpty() {
        return transactions.empty();
    }

    Transaction pop() {
        if (!transactions.empty()) {
            Transaction t = transactions.top();
            transactions.pop();
            return t;
        } else {
            cout << "⚠️ No transaction to undo.\n";
            return {"none", -1};
        }
    }

    void viewTransactions() {
        if (transactions.empty()) {
            cout << "🕒 No transactions yet.\n";
            return;
        }

        cout << "\n📜 Recent Transactions:\n";
        stack<Transaction> temp = transactions;
        int count = 1;
        while (!temp.empty()) {
            Transaction t = temp.top();
            cout << count++ << ". " << t.type << " | Book ID: " << t.bookID << endl;
            temp.pop();
        }
    }
};
class LibrarySystem {
private:
    BookList bookList;
    TransactionStack transStack;

public:
    void insertBook() {
        int id;
        string title, author;
        cout << "Enter Book ID: ";
        cin >> id;
        cin.ignore();
        cout << "Enter Book Title: ";
        getline(cin, title);
        cout << "Enter Author Name: ";
        getline(cin, author);
        bookList.insertBook(id, title, author);
    }

    void deleteBook() {
        int id;
        cout << "Enter Book ID to delete: ";
        cin >> id;
        bookList.deleteBook(id);
    }

    void issueBook() {
        int id;
        cout << "Enter Book ID to issue: ";
        cin >> id;
        BookNode* book = bookList.searchBook(id);
        if (book != nullptr && book->status == "Available") {
            book->status = "Issued";
            transStack.push("issue", id);
            cout << "📕 Book '" << book->title << "' has been issued.\n";
        } else if (book != nullptr) {
            cout << "⚠️ Book already issued.\n";
        }
    }

    void returnBook() {
        int id;
        cout << "Enter Book ID to return: ";
        cin >> id;
        BookNode* book = bookList.searchBook(id);
        if (book != nullptr && book->status == "Issued") {
            book->status = "Available";
            transStack.push("return", id);
            cout << "📗 Book '" << book->title << "' has been returned.\n";
        } else if (book != nullptr) {
            cout << "⚠️ Book is not issued.\n";
        }
    }

    void undoTransaction() {
        if (transStack.isEmpty()) {
            cout << "⚠️ No transaction to undo.\n";
            return;
        }

        Transaction last = transStack.pop();
        BookNode* book = bookList.searchBook(last.bookID);
        if (book == nullptr) return;

        if (last.type == "issue") {
            book->status = "Available";
            cout << "↩️ Undo: Book '" << book->title << "' is now Available again.\n";
        } else if (last.type == "return") {
            book->status = "Issued";
            cout << "↩️ Undo: Book '" << book->title << "' is marked as Issued again.\n";
        }
    }

    void displayBooks() {
        bookList.displayBooks();
    }

    void viewTransactions() {
        transStack.viewTransactions();
    }
};

int main() {
    LibrarySystem system;
    int choice;

    cout << "==========================================\n";
    cout << "📚 Library Book Management System\n";
    cout << "Using Singly Linked List & Stack (C++)\n";
    cout << "==========================================\n";

    do {
        cout << "\n-------- MENU --------\n";
        cout << "1. Add Book\n";
        cout << "2. Delete Book\n";
        cout << "3. Display Books\n";
        cout << "4. Issue Book\n";
        cout << "5. Return Book\n";
        cout << "6. Undo Last Transaction\n";
        cout << "7. View All Transactions\n";
        cout << "0. Exit\n";
        cout << "----------------------\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: system.insertBook(); break;
            case 2: system.deleteBook(); break;
            case 3: system.displayBooks(); break;
            case 4: system.issueBook(); break;
            case 5: system.returnBook(); break;
            case 6: system.undoTransaction(); break;
            case 7: system.viewTransactions(); break;
            case 0: cout << "👋 Exiting... Goodbye!\n"; break;
            default: cout << "⚠️ Invalid choice! Try again.\n"; break;
        }
    } while (choice != 0);

    return 0;
}