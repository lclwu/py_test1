import itertools
mylist=("".join(x) for x in itertools.product("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",repeat=2))
# while True:
#   print(next(mylist))

# print(type(mylist))



import random
import string
def generate_random_str(randomlength):
    '''
    string.digits = 0123456789
    string.ascii_letters = 26个小写,26个大写
    '''
    str_list = random.sample(string.digits + string.ascii_letters,randomlength)
    random_str = ''.join(str_list)
    return random_str

print(generate_random_str(randomlength=2))


import itertools
mylist=("".join(x) for x in itertools.product("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",repeat=16))
while True:
  print(next(mylist))

r=[1,3,2,1,3]
c=[]
for i in r:
    c.append(r.count(i))
    if r.count(i)>1:
        print(str(i)+'出现过两次')
print(c)


A=[1,2,3,4,5,6]