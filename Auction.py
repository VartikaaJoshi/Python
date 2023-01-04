from replit import clear

auction_dictionary = {}
auction_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is the {winner} of the bid $ {highest_bid}")
            

while not auction_finished:
    
    name = input("What is your name?: ")
    bid = int(input("Please enter your bid: $"))
    auction_dictionary[name] = bid
    other_auctions = input("Is there more people? Type yes or no: ").lower()
    if other_auctions == "no":
        auction_finished = True
        highest_bidder(auction_dictionary)
    elif other_auctions == "yes":
        clear()
