your_name = input("Please enter your name: ")
partner_name = input("Please enter your partner's name: ")

your_name_low = your_name.lower()
partner_name_low = partner_name.lower()

your_name_count1 = your_name.count("t")
your_name_count1= your_name_count1 + your_name.count("r")
your_name_count1= your_name_count1 + your_name.count("u")
your_name_count1= your_name_count1 + your_name.count("e")

partner_name_count1 = partner_name.count("t")
partner_name_count1 = partner_name_count1 + partner_name.count("r")
partner_name_count1 = partner_name_count1 + partner_name.count("u")
partner_name_count1 = partner_name_count1 + partner_name.count("e")

your_name_count2 = your_name.count("l")
your_name_count2= your_name_count2 + your_name.count("o")
your_name_count2= your_name_count2 + your_name.count("v")
your_name_count2= your_name_count2 + your_name.count("e")

partner_name_count2 = partner_name.count("l")
partner_name_count2 = partner_name_count2 + partner_name.count("o")
partner_name_count2 = partner_name_count2 + partner_name.count("v")
partner_name_count2 = partner_name_count2 + partner_name.count("e")

true_match = your_name_count1 + partner_name_count1
love_match = your_name_count2 + partner_name_count2

true = str(true_match)
love = str(love_match)
print("Your Love score is :" + true + love)
