import random
import string
import pytest
from auctionengine.tracker import SimpleTracker
from .test_simpletracker import random_name

def test_negative_zero_bid():
   tracker = SimpleTracker()
   user = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   with pytest.raises(ValueError):
      user.bid_on(item, -1)

   with pytest.raises(ValueError):
      user.bid_on(item, 0)

   assert len(user.items_bid) == 0
   assert len(item.bids) == 0
   assert item.get_winning_bid() is None

def test_placing_bid():
   tracker = SimpleTracker()
   user1 = tracker.create_user(random_name(20))
   user2 = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   valid_bids = 0
   
   for i in range(20):
      for u in [user1, user2]:
         if u.bid_on(item, random.randint(1,100)):
            valid_bids = valid_bids + 1

   assert len(item.bids) == valid_bids

def test_winning_bid():
   tracker = SimpleTracker()
   user = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   for i in range(1, 20):
      user.bid_on(item, i)

   winning_bid = item.get_winning_bid()
   assert winning_bid.price == 19
   assert winning_bid.bidder == user

def test_has_bid_on():
   tracker = SimpleTracker()
   user = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   assert user.has_bid_on(item) == False
   
   user.bid_on(item, 1)
   assert user.has_bid_on(item) == True

def test_is_highest_bidder():
   tracker = SimpleTracker()
   user1 = tracker.create_user(random_name(20))
   user2 = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   assert user1.is_highest_bidder(item) == False
   
   user1.bid_on(item, 1)
   assert user1.is_highest_bidder(item) == True
   
   user2.bid_on(item, 2)
   assert user1.is_highest_bidder(item) == False
   assert user2.is_highest_bidder(item) == True

def test_items_user_has_bid():
   tracker = SimpleTracker()
   user = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   assert len(user.items_bid) == 0

   user.bid_on(item, 1)
   assert len(user.items_bid) == 1

   user.bid_on(item, 2)
   assert len(user.items_bid) == 1
   
