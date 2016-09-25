import random
import string
import pytest
from auctionengine import tracker

def random_name(length):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(length))

def test_user_creation():
    tracker.users = []
    assert len(tracker.users) == 0

    user_names = [random_name(random.randint(1, 20)) for n in range(100)]
    
    for name in user_names:
        user = tracker.create_user(name)
        assert user is not None
        assert user.name == name

    assert len(tracker.users) == len(user_names)
    
    with pytest.raises(ValueError):
        tracker.create_user("")

    tracker.users = []

def test_item_creation():
    tracker.items = []
    assert len(tracker.items) == 0

    item_names = [random_name(random.randint(1, 20)) for n in range(100)]
    
    for name in item_names:
        item = tracker.create_item(name)
        assert item is not None
        assert item.name == name

    assert len(tracker.items) == len(item_names)

    with pytest.raises(ValueError):
        tracker.create_item("")

    tracker.items = []
