# -------------------------------
# STRING METHODS
# -------------------------------
# name = input("Enter your name: ")
# phone_number = input("Enter your phone #: ")

# length = len(name)
# index = name.find(" ")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count(" ")
# phone_number = phone_number.replace("-", "")

# -------------------------------
#        EXERCISE
# -------------------------------
username = input("Enter a username: ")

if len(username) > 12:
    print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digits")
else:
    print(f"Welcome {username}!")


# ---------------------------------------
# New Keywords:

# len(name)                     retruning the length of the string
# str.find("value")             finding a substring
# str.rfind("value")            reversed finding
# str.capitalize()              making the first character of each word upper case
# str.upper()                   returning all characters upper case
# str.lower()                   returning all characters lower case
# str.isdigit()                 containing only digits
# str.isalpha()                 containing only alphabet
# str.count("value")            counting a substring within a string
# str.replace("old", "new")     replacing the first value with the second one
# help()



