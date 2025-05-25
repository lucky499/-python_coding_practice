# # Enter your code here. Read input from STDIN. Print output to STDOUT
# from itertools import combinations_with_replacement

# s, k = input().split(" ")
# #print(istr)
# string_tuple_list = list(combinations_with_replacement(sorted(s), int(k)))
# for tup in string_tuple_list:
#     print(''.join(tup))



## using group by
# Enter your code here. Read input from STDIN. Print output to STDOUT

# from itertools import groupby

# s = input()
# tups = groupby(s)
# for k, i in tups:
#     print(f"{(len(list(i)), int(k))} ", end="")


from itertools import groupby

s = "jaaalskdlasslkdddddllllliiiii"
tups = groupby(s)
for k, i in tups:
    print(f"{k}{len(list(i))}", end="" )


# name: list[str] = ['mac', 'windows', 'linux', 'google', 'bing']
# names_with_len_less_five = groupby(name, key=lambda x: len(x)<5)
# for k, i in names_with_len_less_five:
#     if k:
#         print(list(i))
# print(names_with_len_less_five)







