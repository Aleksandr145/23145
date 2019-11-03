# why i don't know
a = [1,2,3,4,5,6,7,8,9]
b = [1,"two",3,4.4,["d","T"],(9,8)]
t = 1,2,3
x = 0.125
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator) # finally we have some insight into the classic
# stupid Python for swapping two variables!
for i in range(50):
    print(a,b,t)
print(x.as_integer_ratio()) #return value can be indidually
print(a)
print(b)
print(t)
input('Wait...')
