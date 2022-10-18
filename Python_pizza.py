print("Welcome to Python Pizza")

type = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want Pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
if type == "S":
  price = 15

elif type =="M":
  price = 20

elif type =="L":
  price = 25

if pepperoni == "Y":
  if type== "S":
    new_price = price + 2
  else:
    new_price = price + 3
else:
  new_price = price

if cheese == "Y":
  bill= new_price + 1

else:
  bill = new_price

bill_amount = str(bill)
print("Please pay $" + bill_amount)
