import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or get the database
database = client["PayrollDatabase"]

print("Connected to MongoDB!")

# You can create collections and documents as needed within the "payroll" database.
# For example, to create a collection named "employees":
employees_collection = database["PayrollCollection"]

# Now you can insert documents into the "employees" collection, for example:
# employee_data = {
#     "name": "John Doe",
#     "position": "Software Engineer",
#     "salary": 60000
# }

# Insert the document into the collection
# employees_collection.insert_one(employee_data)

print("Document inserted successfully!")

# Close the MongoDB connection when you're done
client.close()
