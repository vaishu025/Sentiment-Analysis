from pymongo import MongoClient

# MongoDB Atlas Connection
client = MongoClient("YOUR_MONGODB_CONNECTION_STRING")

db = client["sentiment_analysis"]
collection = db["reviews"]

# Sample Data
reviews = [
    {"text": "This product is amazing!", "sentiment": "Positive"},
    {"text": "I love this service.", "sentiment": "Positive"},
    {"text": "The quality is average.", "sentiment": "Neutral"},
    {"text": "I am disappointed with the product.", "sentiment": "Negative"},
    {"text": "Very bad experience.", "sentiment": "Negative"}
]

# Insert Data
collection.insert_many(reviews)

print("Data inserted successfully!")
