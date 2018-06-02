
import pymongo
from models.database import Database
#from models.post import Post
from models.blog import Blog

__author__ = 'chance'

Database.initialize()

uri = "mongodb://127.0.0.1:27017"

# Start mongod from Git CMD
client = pymongo.MongoClient(uri)
database = client['fullstack']


blog = Blog(author="Chance",
            title="Title",
            description="Description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts()) # like Post.from_blog(id)











#collection = database['students']
#students = [ student for student in collection.find({})]
#print(students)

#post = Post(blog_id = "234")

#post.save_to_mongo()

#posts = Post.from_blog("123")

#for post in posts:
#    print( post)

