# Auction Engine Exercise [![Build Status](https://travis-ci.org/kostaspl/stratagem_auction_engine.svg?branch=master)](https://travis-ci.org/kostaspl/stratagem_auction_engine)
The aim of this project is to design a very simple object-oriented Auction Engine.

## [tracker.py](auctionengine/tracker.py)
`Tracker` is an abstract class, implemented using the `abc` module. 
It has 2 methods, `create_user` and `create_item`.

Two implementations of `Tracker` are included:
`SimpleTracker` uses lists to store new `User`s and `Item`s.
`UniqueTracker` does the same, but makes sure no `User` or `Item` exists with the same name.

## [user.py](auctionengine/user.py)
`User` is a class with `name` and `items_bid` attributes. 
`name` **cannot** be an empty string.
`items_bid` is a set of the `Item`s on which this `User` has placed a bid.
Available methods are `bid_on`, `has_bid_on` and `is_highest_bidder`.

## [item.py](auctionengine/item.py)
`Item` is a class with `name` and `bids` attributes.
`name` **cannot** be an empty string.
`bids` is a list of all the bids placed on this `Item`.
Available methods are `bid` and `get_winning_bid`.

## [bid.py](auctionengine/bid.py)
`Bid` is a class with `bidder`, `price` and `item` attributes.
`price` **must** be greater than 0. 
`bidder` and `item` **cannot** be `None`.