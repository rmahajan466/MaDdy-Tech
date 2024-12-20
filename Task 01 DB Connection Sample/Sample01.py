# MySQL Example: File System to Database
# This script demonstrates connecting to a MySQL database, inserting data, and closing the connection.
import mysql.connector

def mysql_example():
    """
    Connects to a MySQL database, inserts a record into a table, and closes the connection.
    """
    try:
        # Create DB Connection
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sample_db"
        )
        mysql_cursor = mysql_conn.cursor()
        print("Connected to MySQL.")

        # Push Data
        mysql_cursor.execute("INSERT INTO sample_table (name, contact) VALUES (%s, %s)", ("Raghav", 7566364655))
        mysql_conn.commit()
        print("Data pushed to MySQL.")

    except Exception as e:
        print("MySQL Error:", e)

    finally:
        # Close Connection
        if mysql_cursor:
            mysql_cursor.close()
        if mysql_conn:
            mysql_conn.close()
        print("MySQL connection closed.")

if __name__ == "__main__":
    print("--- MySQL Sample ---")
    mysql_example()