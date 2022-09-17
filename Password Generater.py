import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "[]{}!@£$%^&*()|?><:;"

all=lower + upper + NUMBER + Symbol
# The number the length, that is how many character you password is going to be
length = 8
password = "".join(random.sample(all,length))
print(" The Password You Generated Is :",password)
