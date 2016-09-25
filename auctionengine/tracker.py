from .user import User
from .item import Item

items = []
users = []

def create_item(name):
    item = Item(name)
    items.append(item)
    return item

def create_user(name):
    user = User(name)
    users.append(user)
    return user
