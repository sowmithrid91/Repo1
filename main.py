# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
from Github import Github
# Login account
git=Github("sowmithrid91","Enjoyyear@2022.")
import subprocess
from pathlib import Path

user = git.get_user()
# Create a new branch
Branch = input("Enter a branch name")
repo.git.branch(Branch)
# You need to check out the branch after creating it if you want to use it
repo.git.checkout('Branch')
# create a new repo
re = input("Enter a folder name")
repo = user.create_repo(re)
# Commit the file
repo.git.add('--all')
repo.git.commit('-m', 'commit message from python script', author='test_user@test.com')
origin = repo.remote(name='origin')
origin.push()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
