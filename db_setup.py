import sqlite3
from pathlib import Path

# -----------------------------
# 1. Decide where the database file will live
# -----------------------------
DB_PATH = Path(__file__).parent / "expenditures.db"

try:
    # -----------------------------
    # 2. Connect to the SQLite database
    # -----------------------------
    # If the file doesn't exist, SQLite will create it.
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # -----------------------------
    # 3. Define the SQL statement to create the table
    # -----------------------------
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        item TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        type TEXT NOT NULL,
        notes TEXT
    );
    """

    # -----------------------------
    # 4. Execute the SQL statement
    # -----------------------------
    cursor.execute(create_table_sql)

    # -----------------------------
    # 5. Commit the change
    # -----------------------------
    connection.commit()

    # -----------------------------
    # 6. Query the database for the table structure
    # -----------------------------
    # PRAGMA table_info returns one row per column in the table.
    cursor.execute("PRAGMA table_info(transactions);")
    table_info = cursor.fetchall()

    # -----------------------------
    # 7. Print the table structure
    # -----------------------------
    print("\nTable 'transactions' structure:")
    for column in table_info:
        # Each column tuple looks like:
        # (column_id, name, type, notnull, default_value, primary_key_flag)
        print(column)

    # -----------------------------
    # 8. Print success message
    # -----------------------------
    print(f"\nDatabase created (or opened) at: {DB_PATH}")
    print("Table 'transactions' has been created successfully.\n")

except Exception as e:
    # -----------------------------
    # 9. Catch any errors and print them
    # -----------------------------
    print("\nERROR: Something went wrong while creating the database or table.")
    print(f"Details: {e}\n")

finally:
    # -----------------------------
    # 10. Close the connection if it was opened
    # -----------------------------
    try:
        connection.close()
    except:
        pass
