import sys

# print(dir(sys))

a = [1,2,3,4,5,6]
io = iter(a)
print(type(io))
print(next(io))