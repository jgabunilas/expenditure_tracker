import sqlite3
from pathlib import Path

# ------------------------------------------------------------
# 1. Decide where the database file will live
# ------------------------------------------------------------
# Path(__file__).parent gives us the folder where THIS script lives.
# We then append "expenditures.db" to that folder path.
# This ensures the database file sits right next to db_setup.py.
DB_PATH = Path(__file__).parent / "expenditures.db"

try:
    # ------------------------------------------------------------
    # 2. Connect to the SQLite database
    # ------------------------------------------------------------
    # sqlite3.connect() opens the database file.
    # If the file does not exist, SQLite automatically creates it.
    #
    # The returned object is a "connection" — it represents our link
    # to the database file. We use it to send commands and save changes.
    connection = sqlite3.connect(DB_PATH)

    # ------------------------------------------------------------
    # 3. Create a "cursor" object
    # ------------------------------------------------------------
    # A cursor is like a "command tool" or "remote control" for the database.
    #
    # You cannot send SQL commands directly to the connection.
    # Instead, you hand the commands to the cursor, and the cursor
    # delivers them to the database.
    #
    # Think of:
    #   - connection = the database itself
    #   - cursor = the thing that sends commands to the database
    cursor = connection.cursor()

    # ------------------------------------------------------------
    # 4. Define the SQL statement to create the table
    # ------------------------------------------------------------
    # This is a normal SQL CREATE TABLE command.
    # IF NOT EXISTS prevents errors if the table already exists.
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

    # ------------------------------------------------------------
    # 5. Execute the SQL statement
    # ------------------------------------------------------------
    # cursor.execute(sql) sends the SQL command to the database.
    #
    # The database reads the command and performs the action
    # (in this case, creating the table if it doesn't already exist).
    cursor.execute(create_table_sql)

    # ------------------------------------------------------------
    # 6. Commit the change
    # ------------------------------------------------------------
    # connection.commit() tells SQLite:
    #   "Save everything we've done so far to the database file."
    #
    # Without commit(), the changes might not be written to disk.
    connection.commit()

    # ------------------------------------------------------------
    # 7. Query the database for the table structure
    # ------------------------------------------------------------
    # PRAGMA table_info(table_name) is a special SQLite command.
    #
    # It returns one row per column in the table, describing:
    #   - column ID
    #   - column name
    #   - column type
    #   - whether NULL is allowed
    #   - default value
    #   - whether it is a primary key
    #
    # We again use cursor.execute() to send this command.
    cursor.execute("PRAGMA table_info(transactions);")

    # ------------------------------------------------------------
    # 8. Fetch the results
    # ------------------------------------------------------------
    # cursor.fetchall() retrieves ALL rows returned by the last query.
    #
    # In this case, it returns a list of tuples.
    # Each tuple describes one column in the table.
    #
    # Example of one tuple:
    #   (0, 'id', 'INTEGER', 0, None, 1)
    #
    # fetchall() is how we "read" results from the database.
    table_info = cursor.fetchall()

    # ------------------------------------------------------------
    # 9. Print the table structure
    # ------------------------------------------------------------
    print("\nTable 'transactions' structure:")
    for column in table_info:
        print(column)

    # ------------------------------------------------------------
    # 10. Print success message
    # ------------------------------------------------------------
    print(f"\nDatabase created (or opened) at: {DB_PATH}")
    print("Table 'transactions' has been created successfully.\n")

except Exception as e:
    # ------------------------------------------------------------
    # 11. Catch any errors and print them
    # ------------------------------------------------------------
    print("\nERROR: Something went wrong while creating the database or table.")
    print(f"Details: {e}\n")

finally:
    # ------------------------------------------------------------
    # 12. Close the connection if it was opened
    # ------------------------------------------------------------
    # Closing the connection releases the database file.
    # We wrap this in a try/except in case connection was never created.
    try:
        connection.close()
    except:
        pass
