
age = input("What is your current age?")

age1 = int(age)
avg_lifespan = 85

years_left = avg_lifespan - age1

months_left = years_left * 12

weeks_left = (years_left * 365) / 7

years_left1 = str(years_left)
months_left1 = str(months_left)
weeks_left1 = str(weeks_left)

print("You have " + years_left1 + "yrs, " + months_left1 + "months and " +
      weeks_left1 + " weeks left.")
