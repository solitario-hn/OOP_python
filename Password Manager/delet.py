# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# nr_letters = random.randint(8, 10)
# nr_symbols = random.randint(2, 4)
# nr_numbers = random.randint(2, 4)

# password_letter = [random.choice(letters) for _ in range(nr_letters)]
# print(password_letter)
# password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
# print(password_symbols)
# password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
# print(password_symbols)
# password_list=password_letter+password_symbols+password_numbers
# print(password_list)
# random.shuffle(password_list)

# password = "".join(password_list)    #this will join each elemnt in the list and return it in string format.
# print(f"Your password is: {password}")

# password = ""
# for char in password_list:
#   password += char
# for char in password_symbols:
#     password+=char
# for char in password_numbers:
#     password+=char

def func(name:str):
    return "name" + 123


func(6879)