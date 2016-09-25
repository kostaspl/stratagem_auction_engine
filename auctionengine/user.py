class User:
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("User name must not be empty")
        self.name = name
        self.items_bid = set()

    def bid_on(self, item, price):
        if (item.bid(self, price)):
            self.items_bid.add(item)
            return True
        return False

    def has_bid_on(self, item):
        return item in self.items_bid

    def is_highest_bidder(self, item):
        if not self.has_bid_on(item):
            return False
        return item.get_winning_bid().bidder == self

    def __str__(self):
        return "%s" % (self.name)
