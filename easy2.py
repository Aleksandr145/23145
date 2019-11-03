primes = [1,12,3,5,6,7,['a']]

words = ['plural','nose','salt','prepare','broad',
'require','gray','maind','wrong',
'select',help(str)] # help discription function
primes[2] = 'ss' # this help change number or ather
words[7] = 'OOO'
print(help(words))
print("salt" in words) # show have or not have : False or True
print(words.pop())# list.pop() - show last element of a list
print(words.index('gray'))
print(len(words))# show how much all object
print(primes)
print(words[7:])# this help show from list what do you need; -,:,
print(words[1:-1])# -1 first a word

input("Wait...")
