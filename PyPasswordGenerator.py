import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')' '+']

print("\nWelcome to the PyPassword Generator! \n\n")
nbr_letters = int(input("How Many Letter Would You Like In Your Password?:\n"))
nbr_symbols = int(input("How Many Symbols Would You Want? :\n"))
nbr_numbers = int(input("How Many Numbers Would You Like In Your Password?:\n"))

# # Easy Level that is the password will not be random.
#
# password = ""
# for char in range(1, nbr_letters + 1):
#     password += random.choice(letters)
#
# for char in range(1, nbr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nbr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)

# Hard Level that is randomly selects from letters, symbols and letters with no specified order.

password_list = []
for char in range(1, nbr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nbr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nbr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
#the above print does not print the password in a random manner

random.shuffle(password_list)
print(password_list)
# password is random but in a list form.

# converting the list back into a string
password = ""
for char in password_list:
    password += char

print(f"Your Password is: {password}")
