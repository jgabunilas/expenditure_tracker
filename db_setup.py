# This file establishes the SQLite database and connects to it
# Created with VIBE coding using MS Copilot

import sqlite3  # This is Python's built-in library for working with SQLite databases
from pathlib import Path  # This helps us work with file paths in a clean, cross-platform way

# -----------------------------
# 1. Decide where the database file will live
# -----------------------------

# Here, we're saying: "Put the database file in the same folder as this script."
# You can change the name 'expenditures.db' if you prefer something else.
DB_PATH = Path(__file__).parent / "expenditures.db"

# -----------------------------
# 2. Connect to the SQLite database (or create it if it doesn't exist)
# -----------------------------

# sqlite3.connect() will:
# - open the database file if it already exists
# - create a new file if it does NOT exist
# The result is a "connection" object that lets us talk to the database.
connection = sqlite3.connect(DB_PATH)

# -----------------------------
# 3. Create a "cursor" object
# -----------------------------

# A cursor is like a "command runner" for the database.
# We use it to execute SQL statements (like CREATE TABLE, INSERT, SELECT, etc.).
cursor = connection.cursor()

# -----------------------------
# 4. Define the SQL statement to create the 'transactions' table
# -----------------------------

# This SQL statement describes the structure of our main table.
# It will only create the table if it does NOT already exist.
create_table_sql = """
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each transaction, assigned automatically
    date TEXT NOT NULL,                    -- Date of the transaction, stored as text in 'YYYY-MM-DD' format
    item TEXT NOT NULL,                    -- Description of what this transaction is (e.g., 'Rent', 'Groceries')
    category TEXT NOT NULL,                -- Category (e.g., 'Housing', 'Auto', 'Restaurants')
    amount REAL NOT NULL,                  -- Dollar amount (negative for expenses, positive for income/credits)
    type TEXT NOT NULL,                    -- Type of transaction: 'expense', 'income', 'credit', 'refund'
    notes TEXT                             -- Optional notes for extra details (can be left empty)
);
"""

# -----------------------------
# 5. Execute the SQL statement to create the table
# -----------------------------

# This line sends the CREATE TABLE command to the database.
cursor.execute(create_table_sql)

# -----------------------------
# 6. Save (commit) the changes to the database
# -----------------------------

# Even though CREATE TABLE is a structural change, we still commit it
# so that the table definition is permanently stored in the database file.
connection.commit()

# -----------------------------
# 7. Close the connection
# -----------------------------

# It's good practice to close the connection when we're done.
# This releases the file and ensures everything is clean.
connection.close()

# -----------------------------
# 8. Print a friendly message so we know it worked
# -----------------------------

print(f"Database created (or opened) at: {DB_PATH}")
print("Table 'transactions' has been created (if it did not already exist).")