import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special =string.punctuation
    charaters=letters
    if numbers:
        charaters+=digits
    if special_characters:
        charaters+=special
    pwd=""
    meet=False
    nn=False
    sp=False
    while not meet or len(pwd)<min_length:
        new_char=random.choice(charaters)
        pwd+=new_char

        if new_char in digits:
            nn=True
        elif new_char in special:
            sp=True

        meet=True
        if numbers:
            meet=nn
        if special_characters:
            meet=meet and sp
    return pwd
min_length=int(input('enter the minimum length:'))
nn=input('do you want to have a numbers(y/n)?').lower()=="y"
sp=input('do you want to have special charaters(y/n)').lower()=="y"
pwd=generate_password(min_length,nn,sp)
print("the generate password is",pwd)

