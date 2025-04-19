# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

save_dic = {}
def get_user():
    name = input("What is your name? ").lower()
    bid = int(input("What is your bid? $ "))
    return name, bid

def add_new_buyer():
    name, bid = get_user()  # unpack returned values
    save_dic[name] = bid    # save to main dictionary

highest_bid = 0
winner = ""
bid_finish=False
while not bid_finish:
    add_new_buyer()
    print(save_dic)
    ask = input("Are there other bidders? Type Yes or No: ").lower()
    if ask == "no":
        bid_finish = True

for name ,bid in save_dic.items():
    if bid>highest_bid:
        highest_bid = bid
        winner = name
print(f"🏆 The winner is {winner} with a bid of ${highest_bid}")









