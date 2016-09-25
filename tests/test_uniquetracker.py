import random
import string
import pytest
from auctionengine.tracker import UniqueTracker

def test_user_creation():
    tracker = UniqueTracker()
    assert len(tracker.users) == 0

    with pytest.raises(ValueError):
        tracker.create_user("")

    assert tracker.create_user("TestUser") is not None

    with pytest.raises(ValueError):
        tracker.create_user("TestUser")


def test_item_creation():
    tracker = UniqueTracker()
    assert len(tracker.items) == 0

    with pytest.raises(ValueError):
        tracker.create_item("")

    assert tracker.create_item("TestItem") is not None

    with pytest.raises(ValueError):
        tracker.create_item("TestItem")
