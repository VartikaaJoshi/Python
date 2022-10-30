def format_name():

    first_name = f_name.title()
    last_name = l_name.title()
    

    print("Your formatted name is: " + first_name +" " +last_name)

f_name = input("What is your first name? ").lower()
l_name = input("What is your last name? ").lower()


format_name()
