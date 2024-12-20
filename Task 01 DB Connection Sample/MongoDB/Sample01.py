# MongoDB Example: File System to Database
# This script demonstrates connecting to a MongoDB database, inserting a document, and closing the connection.
from pymongo import MongoClient

def mongodb_example():
    """
    Connects to a MongoDB database, inserts a document, and closes the connection.
    """
    try:
        # Create DB Connection
        mongo_client = MongoClient("mongodb+srv://MaDdyTech:MaDdyTech@sample-db.2lxd0.mongodb.net/?retryWrites=true&w=majority&appName=sample-db")
        mongo_db = mongo_client["sample-db"]
        mongo_collection = mongo_db["test_collection"]
        print("Connected to MongoDB.")

        # Push Data
        mongo_collection.insert_one({"name": "example", "Raghav": 123})
        print("Data pushed to MongoDB.")

    except Exception as e:
        print("MongoDB Error:", e)

    finally:
        # Close Connection
        if mongo_client:
            mongo_client.close()
        print("MongoDB connection closed.")

if __name__ == "__main__":
    print("--- MongoDB Example ---")
    mongodb_example()