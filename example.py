import random
from auctionengine.tracker import SimpleTracker

if __name__ == "__main__":
    tracker = SimpleTracker()
    
    tracker.create_item("iPhone")
    tracker.create_item("PlayStation")
    tracker.create_item("XBOX")
    tracker.create_item("MacBook")
    tracker.create_item("Note7")
    tracker.create_item("iPad")
    tracker.create_item("ZenBook")

    print("Printing tracker items...")
    for i in tracker.items:
        print(i)

    tracker.create_user("Kostas")
    tracker.create_user("John")
    tracker.create_user("George")
    tracker.create_user("Nick")

    print("\nPrinting tracker users...")
    for u in tracker.users:
        print(u)

    # test 20 random bids
    print("\nAttempting 20 random bids...")
    for i in range(20):
        # pick a random price from 1 to 100
        price = random.randint(1, 100)
        # pick a random user
        user = random.choice(tracker.users)
        # pick a random item
        item = random.choice(tracker.items)
        # do not bid if already the highest bidder
        if (user.has_bid_on(item) and item.get_winning_bid().bidder == user):
            print("{} skipped bidding because he is already the highest bidder for {}".format(user, item))
            continue
        # try to place bid
        if (user.bid_on(item, price)):
            print("{} successfully bid on {} for {}".format(user, item, price))
        else:
            print("{} failed to bid on {} for {}. Current winning bid price is {}".format(user, item, price, item.get_winning_bid().price))

    print("\nPrinting winning bids for every item...")
    for i in tracker.items:
        winning_bid = i.get_winning_bid()
        if (winning_bid is None):
            print("No one bid on", i.name)
            continue
        print("Winning bid for {}: {} by {}".format(i.name, winning_bid.price, winning_bid.bidder.name))

    print("\nPrinting all bids for every item...")
    for i in tracker.items:
        if len(i.bids) == 0:
            print("No bids for", i.name)
            continue
        print("Bids for", i.name)
        for b in i.bids:
            print("\t", b)

    print("\nPrinting all items each user has bid on...")
    for u in tracker.users:
        if len(u.items_bid) == 0:
            print("{} has placed no bids".format(u.name))
            continue
        print("{} has bid on:".format(u.name))
        for i in u.items_bid:
            print("\t", i.name)
