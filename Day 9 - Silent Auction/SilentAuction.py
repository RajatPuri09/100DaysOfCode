from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art
print(art.logo)

auction = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    Aname = input("Enter your name...\n")
    bid = int(input("Enter your bid...\n"))
    auction[Aname] = bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(auction)
    elif should_continue == "yes":
        clear()
    
