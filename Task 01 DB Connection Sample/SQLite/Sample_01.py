# SQLite Example: File System to Database
# This script demonstrates connecting to an SQLite database, creating a table, inserting data, and closing the connection.
import sqlite3

def sqlite_example():
    """
    Connects to an SQLite database, creates a table, inserts a record, and closes the connection.
    """
    try:
        # Create DB Connection
        sqlite_conn = sqlite3.connect("sample_db.sqlite")
        sqlite_cursor = sqlite_conn.cursor()
        print("Connected to SQLite.")

        # Create Table and Push Data
        sqlite_cursor.execute("CREATE TABLE IF NOT EXISTS test_table (name TEXT, value INTEGER)")
        sqlite_cursor.execute("INSERT INTO test_table (name, value) VALUES (?, ?)", ("Raghav", 123))
        sqlite_conn.commit()
        print("Data pushed to SQLite.")

    except Exception as e:
        print("SQLite Error:", e)

    finally:
        # Close Connection
        if sqlite_conn:
            sqlite_conn.close()
            print("SQLite connection closed.")

if __name__ == "__main__":
    print("--- SQLite Sample ---")
    sqlite_example()