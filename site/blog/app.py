
import pymongo

from menu import Menu
from models.database import Database
from models.blog import Blog

__author__ = 'chance'
Database.initialize()

menu = Menu()

menu.run_menu()



