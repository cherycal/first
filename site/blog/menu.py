from models.database import Database
from models.blog import Blog

__author__ = 'chance'



class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name:")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()


    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title: str = input("Enter title: ")
        descripton = input()
        blog = Blog(author=self.user,
                    title=title,
                    descripton=descripton)
        blog.save_to_mongo()
        self.user_blog = blog


    def run_menu(self):
        read_or_write = input("Read or write: ")
        if read_or_write == 'R':
            pass
            #     list blogs
            #     allow user to choose one
            #     display posts
        elif read_or_write == 'W':
            pass
            #    Prompt for post
            #
        else:
            pass

