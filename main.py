from fastapi import FastAPI, HTTPException
from pathlib import Path
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Group B!"}

DB_FILE = Path("library_db.json")


def load_data():
    if not DB_FILE.exists():
        return {
            "students": [],
            "books": [],
            "loans": []
        }

    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------
# READ – Students
# ---------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int):
    data = load_data()

    for student in data["students"]:
        if student["StudentID"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/students")
def list_students():
    data = load_data()
    return data["students"]


# ---------------------------
# READ – Books
# ---------------------------

@app.get("/books/{book_id}")
def get_book(book_id: int):
    data = load_data()

    for book in data["books"]:
        if book["BookID"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books")
def list_books():
    data = load_data()
    return data["books"]


# ---------------------------
# READ – Loans
# ---------------------------

@app.get("/loans/{loan_id}")
def get_loan(loan_id: int):
    data = load_data()

    for loan in data["loans"]:
        if loan["LoanID"] == loan_id:
            return loan

    raise HTTPException(status_code=404, detail="Loan not found")


@app.get("/loans")
def list_loans():
    data = load_data()
    return data["loans"]
