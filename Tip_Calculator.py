print("Welcome to the tip calculator")
bill_amount = input("What was your total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

bill_amount1 = float(bill_amount)
tip1 = float(tip)
num_people1 = float(num_people)

total_bill = bill_amount1 + (bill_amount1 * tip1)/100
each_share = total_bill / num_people1
final_amount = round(each_share, 2)
each_share1 = str(final_amount)
print("Each people should pay: $" + each_share1)
