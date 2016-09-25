from .user import User
from .item import Item
from abc import ABC, abstractmethod

class Tracker(ABC):
    @abstractmethod
    def create_item(self, name):
        pass

    @abstractmethod
    def create_user(self, name):
        pass

'''
A very simple Tracker implementation.
'''
class SimpleTracker(Tracker):
    def __init__(self):
        self.items = []
        self.users = []
        
    def create_item(self, name):
        item = Item(name)
        self.items.append(item)
        return item

    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

'''
A Tracker that does not allow user or items with the same name.
'''
class UniqueTracker(Tracker):
    def __init__(self):
        self.items = []
        self.users = []

    def has_item(self, name):
        return name in [n.name for n in self.items]

    def has_user(self, name):
        return name in [n.name for n in self.users]
        
    def create_item(self, name):
        if self.has_item(name):
            raise ValueError("Cannot have 2 items with the same name")
        item = Item(name)
        self.items.append(item)
        return item

    def create_user(self, name):
        if self.has_user(name):
            raise ValueError("Cannot have 2 users with the same name")
        user = User(name)
        self.users.append(user)
        return user
