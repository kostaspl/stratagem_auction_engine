import random
import string
import pytest
from auctionengine.bid import Bid
from auctionengine.user import User
from auctionengine.item import Item

def test_invalid_bid():
   with pytest.raises(ValueError):
      Bid(None, Item("test"), 1)

   with pytest.raises(ValueError):
      Bid(User("test"), None, 1)

   with pytest.raises(ValueError):
      Bid(User("test"), Item("test"), -1)

   with pytest.raises(ValueError):
      Bid(User("test"), Item("test"), 0)
