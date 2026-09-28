# Library Management System

A simple command-line library management application built with Python using classes, functions, modules, JSON storage, and custom exceptions.

## Features

- Add books
- Add members
- Search for books by title, author, or genre
- Borrow and return books
- View member borrowing history
- Persist all data to `data.json`

## Project Structure

```text
library/
├── main.py
├── models.py
├── services.py
├── storage.py
├── data.json
├── README.md
└── .gitignore
```

## Running the App

```bash
python main.py
```

## Example Commands

From the menu, you can:

1. Add a book
2. Add a member
3. View all books
4. View all members
5. Search books
6. Borrow a book
7. Return a book
8. View borrowed books
9. Exit

## Notes

The application stores library data in JSON format, so the state is preserved between runs.

## GitHub

Initialize a repository and push it to GitHub:

```bash
git init
git add .
git commit -m "Initial library management system"
git branch -M main
git remote add origin <your-github-repository-url>
git push -u origin main
```
