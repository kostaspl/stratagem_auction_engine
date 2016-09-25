import random
import string
import pytest
from auctionengine.item import Item

def test_invalid_item():
   with pytest.raises(ValueError):
      Item("")
