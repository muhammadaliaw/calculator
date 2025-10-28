from pymongo import MongoClient
from datetime import datetime

# ---------------- MongoDB Connection ----------------
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "mongotest"           # ✅ your database name
COLLECTION_NAME = "history"     # ✅ your collection name

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

print("✅ Connected to MongoDB")
print("Database:", DB_NAME)
print("Collection:", COLLECTION_NAME)

# ---------------- Helper Function ----------------
def save_to_db(a, b, operation, result):
    """Save each calculation to MongoDB"""
    record = {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    collection.insert_one(record)
    print("✅ Saved to MongoDB:", record)

# ---------------- Calculator Functions ----------------
def add(a, b):
    result = a + b
    save_to_db(a, b, "+", result)
    return result

def subtract(a, b):
    result = a - b
    save_to_db(a, b, "-", result)
    return result

def multiply(a, b):
    result = a * b
    save_to_db(a, b, "*", result)
    return result

def divide(a, b):
    if b == 0:
        print("❌ Error: Division by zero")
        return None
    result = a / b
    save_to_db(a, b, "/", result)
    return result

# ---------------- Menu Loop ----------------
while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("👋 Goodbye!")
        break

    elif choice == "5":
        print("\n--- Calculation History ---")
        for record in collection.find():
            print(record)
        continue

    # Get user input
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        continue

    # Perform selected operation
    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("❌ Invalid choice! Please select from 1–6.")
