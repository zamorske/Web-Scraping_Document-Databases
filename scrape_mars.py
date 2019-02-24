from bs4 import BeautifulSoup
from splinter import Browser
import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_facts_db

# Declare the collection
collection = db.mars_facts_db

# Part I
# A dictionary that represents the document to be inserted
post = {
    'vendor': 'fruit star',
    'fruit': 'raspberry',
    'quantity': 21,
    'ripeness': 2,
    'date': datetime.datetime.utcnow()
}
# Insert the document into the database
collection.insert_one(post)

results = db.mars_facts_db.find()
for result in results:
    print(result)