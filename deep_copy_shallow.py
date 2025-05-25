# Shallow copy: Shallow copy creates a new object but still retains the reference of nested objects. Changes made in nested objects in any of the old or new objects will reflect in another object
# Deep copy: Deep copy creates a new object out of the original object including nested objects. Changes made in new object or old object remains unchanged in another one.

import copy

print("\n\n")
print(" Normal Copy".center(50,"*"))
l1 = [1,2,3,4,5]
l2 = l1
l2[1]=[10,20,30]
print(l1,l2)
print(l1 is l2)
print(l1 == l2)
print(id(l1), id(l2))
print("\n\n")
# print("Shallow Copy".center(50,"*"))
# print(f"{str: 'SHALLOW'^50}")
message = "Shallow Copy"
print(f"{'Shallow Copy':*^50}")
ll1 = [1, [10, 20, 30], 3, 4, 5]
ll2 = copy.copy(ll1)
ll2[2] = 100
print(ll1,ll2)
print(ll1 is ll2)
print(ll1 == ll2)
print(id(ll1), id(ll2))
print("shallo new")
ll1[1][1] = 1000
print(ll1, ll2)
print(id(ll1[3]), id(ll2[3]))


print("\n\n")
print("Deep Copy".center(50,"*"))
dc1 = [1, [10, 20, 30], 3, 4, 5]
dc2 = copy.deepcopy(dc1)
dc2[3]=100
print(dc1,dc2)
print(dc1 is dc2)
print(dc1 == dc2)
print(id(dc1), id(dc2))
print("Deep new")
dc1[1][1] = 2000
print(dc1, dc2)
print(id(dc1[1]), id(dc2[1]))