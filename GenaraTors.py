def genr(n) :
    for i in range (n) :
        yield i # Yield means this function is a generator

g = genr(6)

# for i in g : # For loop will execute all the no. at a time
#     print(i)
#
# print(g) # It will print the location of g

print(g.__next__()) # It will print g at one time
print(g.__next__())
print(g.__next__())