import string
import random

print('------------ RANDOM PASSWORD GENERATOR ------------')

values = string.ascii_letters + string.digits + string.punctuation

pass_len = 12

# list comprehension [function for i in range(n)]
password = "".join([random.choice(values) for i in range(pass_len)])

'''password = ""
for i in range(pass_len):
    choice = random.choice(values)
    password += choice'''

print("Password: ", password)