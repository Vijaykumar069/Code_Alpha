#Password Generator
import random as r
import string as s
def task1(length):
    chars=s.ascii_letters+s.digits+s.punctuation
    password= [r.choice(chars) for i in range(length)]
    return ''.join(password)
input=int(input("Enter the length of the Password : "))
print(task1(input))