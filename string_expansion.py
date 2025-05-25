"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

# s = "This is a test string"
# print(dir(s))

# print(help(s.capitalize))
# sc = s.capitalize
# print(s.capitalize())
 # print(s.count('i'))

# print(s.title())

# # print(help(s.center))

# print(s.endswith('string'))

# print(s.index('i'))

# indexes = [i for i, char in enumerate(s) if char == 'i']
# print(indexes)

# import re

# indcs = re.findall(r'i', s)
# print(indcs)

s = input()
sl = list(s)
# ss = list(s)
index_pos = []  
for i in range(len(sl)):
    if sl[i].isdigit():
        index_pos.append(i)

print(index_pos)
for i in reversed(index_pos):
    mult = int(sl[i])
    sl[i-1] = sl[i-1] * mult
    del sl[i]
print(''.join(sl))


## String compression
from itertools import groupby

s = "jksdddddddddlksksdddddddddddkkkk"
group_obj = groupby(s)
for k, i in group_obj:
    print(f"{k}{len(list(i))}", end="")