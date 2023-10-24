from replit import clear

from art import logo
print(logo)

bidder_dictionary = {}

def add_bidder():
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bidder_dictionary[name] = bid

print("Welcome to the secret auction program.")

response = True

while response == True:

  add_bidder()

  response = input("Are there any othere bidders? Type 'Yes' or 'No'").lower()
  clear()

  if response == 'yes':
    response = True
  else:
    response = False

bidder_name = ""
bidder_value = -1

for key in bidder_dictionary:
  if bidder_dictionary[key] > bidder_value:
    bidder_name = key
    bidder_value = bidder_dictionary[key]

print(f"The winner is {bidder_name} with a bid of ${bidder_value}.")




