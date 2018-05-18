from models.database import Database

__author__ = 'chance'

class Post(object):

    def __init__(self, id, blog_id, date, author=__author__, title="Title", content="DC"):
        self.title = title
        self.content = content
        self.author = author
        self.id = id
        self.blog_id = id
        self.created_date = date

    def save_to_mongo(self):
        Database.insert(collection = 'posts',
                        data = self.json())

    def json(self):
        return{
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }