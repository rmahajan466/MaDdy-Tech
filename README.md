# Database Connection Examples

This repository contains Python scripts demonstrating how to connect to different types of databases (MySQL, SQLite, and MongoDB), perform basic operations, and properly close the connections. Each script is structured with proper documentation and modular design to help you understand the workflow.

## Prerequisites

Before running the scripts, ensure you have the following installed and set up on your system:

- **Python 3.6 or higher**
- Necessary Python libraries:
  - `mysql-connector-python` for MySQL
  - `pymongo` for MongoDB
  - SQLite support is built into Python
- Databases:
  - A MySQL server instance (local or remote)
  - MongoDB server instance (local or remote)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/rmahajan466/MaDdy-Tech.git
   cd your-repo-url
   ```

2. Install the required Python packages:
   ```bash
   pip install mysql-connector-python pymongo
   ```

## Scripts Overview

### MySQL Example

- **File**: `mysql/Sample01.py`
- **Description**: Connects to a MySQL database, inserts a record into a table, and closes the connection.
- **Setup**:
  - Ensure the MySQL server is running.
  - Create a database named `sample_db` and a table named `sample_table` with the following schema:
    ```sql
    CREATE TABLE test_table (
        name VARCHAR(255),
        value INT
    );
    ```
  - Update the connection parameters (host, user, password) in the script.

### SQLite Example

- **File**: `SQLite/Sample_01.py`
- **Description**: Connects to an SQLite database file, creates a table (if it doesn’t exist), inserts a record, and closes the connection.
- **Setup**:
  - No additional setup is needed. The script will create a database file named `sample_db.sqlite` in the project directory.

### MongoDB Example

- **File**: `MongoDB/Sample01.py`
- **Description**: Connects to a MongoDB server, inserts a document into a collection, and closes the connection.
- **Setup**:
  - Ensure the MongoDB server is running.
  - Modify the database name (`sample-db`) and collection name (`test_collection`) in the script if necessary.

## Running the Scripts

To run any of the scripts, execute the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the desired script file name (e.g., `Sample01.py`).

## Example Output

### MySQL Example
```
--- MySQL Example ---
Connected to MySQL.
Data pushed to MySQL.
MySQL connection closed.
```

### SQLite Example
```
--- SQLite Example ---
Connected to SQLite.
Data pushed to SQLite.
SQLite connection closed.
```

### MongoDB Example
```
--- MongoDB Example ---
Connected to MongoDB.
Data pushed to MongoDB.
MongoDB connection closed.
```
