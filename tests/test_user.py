import random
import string
import pytest
from auctionengine.user import User

def test_invalid_user():
   with pytest.raises(ValueError):
      User("")
