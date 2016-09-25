from .bid import Bid

class Item:
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("Item name must not be empty")
        self.name = name
        self.bids = []

    def bid(self, user, price):
        winning_bid = self.get_winning_bid()
        if winning_bid is not None and winning_bid.price >= price:
            return False
        self.bids.append(Bid(user, self, price))
        return True
        
    def get_winning_bid(self):
        if len(self.bids) == 0:
            return None
        return self.bids[-1]

    def __str__(self):
        return "%s" % (self.name)
