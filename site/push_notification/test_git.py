from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
# To find .git directory run git rev-parse --show-toplevel
# /media/sf_Shared/first

repo = Repo("/Ubuntu/Shared/first/")
assert not repo.bare

file = "site/push_notification/file.txt"

git = repo.git

git.add(file)

git.commit('-m','update',file)

git.push()

print( git.status() )



__author__ = 'chance'

print("1")