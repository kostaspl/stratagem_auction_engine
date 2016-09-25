import random
import string
import pytest
from auctionengine import tracker
from .test_tracker import random_name

def test_negative_zero_bid():
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
   user = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   for i in range(1, 20):
      user.bid_on(item, i)

   winning_bid = item.get_winning_bid()
   assert winning_bid.price == 19
   assert winning_bid.bidder == user

def test_has_bid_on():
   user = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   assert user.has_bid_on(item) == False
   
   user.bid_on(item, 1)
   assert user.has_bid_on(item) == True

def test_is_highest_bidder():
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
   user = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   assert len(user.items_bid) == 0

   user.bid_on(item, 1)
   assert len(user.items_bid) == 1

   user.bid_on(item, 2)
   assert len(user.items_bid) == 1

def test_bidding_process():
   user1 = tracker.create_user(random_name(20))
   user2 = tracker.create_user(random_name(20))
   item = tracker.create_item(random_name(20))

   assert len(item.bids) == 0
   assert user1.has_bid_on(item) == False
   assert user1.is_highest_bidder(item) == False
   assert user1.bid_on(item, 10) == True
   assert len(item.bids) == 1
   assert len(user1.items_bid) == 1
   assert user1.has_bid_on(item) == True
   assert user1.is_highest_bidder(item) == True

   winning_bid1 = item.get_winning_bid()

   assert winning_bid1.bidder == user1
   assert winning_bid1.price == 10
   assert len(user1.items_bid) == 1
   
   assert user2.bid_on(item, 10) == False
   assert len(item.bids) == 1
   assert len(user2.items_bid) == 0
   assert user2.has_bid_on(item) == False

   assert user2.bid_on(item, 11) == True
   assert len(item.bids) == 2
   assert len(user2.items_bid) == 1
   assert user2.has_bid_on(item) == True
   assert user1.is_highest_bidder(item) == False
   assert user2.is_highest_bidder(item) == True

   winning_bid2 = item.get_winning_bid()

   assert winning_bid2.bidder == user2
   assert winning_bid2.price == 11

   assert user1.bid_on(item, 12) == True
   assert len(item.bids) == 3
   assert len(user1.items_bid) == 1
   assert user2.is_highest_bidder(item) == False
   assert user1.is_highest_bidder(item) == True
