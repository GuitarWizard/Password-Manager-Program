#Password Generator Project
from random import choice, randint, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# for char in range(nr_letters):
#   password_list.append(random.choice(letters))

# list comprehension format:
# = [new_item for item in list]

password_letters = [choice(letters) for _ in range(randint(3, 10))]
# note there is no item so we just use an '_' in the list comp

password_symbols = [choice(symbols) for _ in range(randint(3, 6))]

password_numbers = [choice(numbers) for _ in range(randint(3, 6))]

password_list = password_numbers + password_letters + password_symbols

shuffle(password_list)

password = ''.join(password_list)

print(f"Your password is: {password}")
