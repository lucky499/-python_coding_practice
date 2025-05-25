l1 = [4,2,6,7,23,7,9,0]

print(sorted(l1, reverse=True, key=lambda x:x%2!=0))
print(l1)

# def squares(x):
#     return x%2 != 0        

# l1.sort(key=squares, reverse=True)
# print(l1)

# def reverse_(l1):
#     list_form = list(l1)
#     start = 0
#     end = len(list_form) - 1
#     while start < end:
#         list_form[start], list_form[end] = list_form[end], list_form[start]
#         end -= 1
#         start += 1
#     return ''.join(list_form)

# names = ["max", "min", "average"]
# sorted_list = list(map(reverse_, names))
# print(sorted_list)

