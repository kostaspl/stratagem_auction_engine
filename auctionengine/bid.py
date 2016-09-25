class Bid:
    def __init__(self, user, item, price):
        if price <= 0:
            raise ValueError("Bid price cannot be negative or zero")
        if user is None:
            raise ValueError("Bidder cannot be None")
        if item is None:
            raise ValueError("Item cannot be None")
        self.bidder = user
        self.price = price
        self.item = item
        
    def __str__(self):
        return "%s bid %d on %s" % (self.bidder.name, self.price, self.item.name)
