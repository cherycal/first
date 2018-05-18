
import pymongo

from models.database import Database
from models.post import Post

__author__ = 'chance'

Database.initialize()

#uri = "mongodb://127.0.0.1:27017"

# Start mongod from Git CMD
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [ student for student in collection.find({})]

print(students)

post = Post("A", "B")
post2 = Post()

print( post.content)

