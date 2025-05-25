# Example:
# [1, 1, 2, 2, 3] → [1, 2, 3]
# [1, 4, 6, 1, 2, 0, 2, 3]
# def sort_the_list(nums):
#     n = len(nums)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         # Swap the elements
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     print(f"Sorted list is: {nums}")
#     return nums

# def remove_dups(numss):
#     nums = sort_the_list(numss)
#     rep_i = 0
#     for i in range(1, len(nums)):
#         if nums[rep_i] != nums[i]:
#             # nums[rep_i] = nums[i]
#             rep_i += 1
#             nums[rep_i] = nums[i]
#     return nums[:rep_i+1]

# numss: list[int] = [1, 4, 6, 1, 2, 0, 2, 3]
# unique_list = list(set(numss))
# unique_list: list[list] = remove_dups(numss)

# print(f"List after removing dups: {unique_list}")
# def uniq_list_finder(nums: list) -> list:
#     uniq_dict: dict = {}
#     uniq_list: list = []
#     for element in nums:
#         if element not in uniq_dict:
#             uniq_list.append(element)
#             uniq_dict[element] = 1
#     return uniq_list




# list_nums: list = [3,5,9,1,0,2,3,5]
# set_nums: set = set(list_nums)
# print(f"printin with set {set_nums}")

# print(f"printing with function: {uniq_list_finder(list_nums)}")



## integer sorting
nums = [1, 4, 6, 1, 2, 0, 2, 3]
for i in range(len(nums)):
    min_index = i
    for j in range(i+1, len(nums)):
        if nums[j] > nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
    print(f"when is {i} -> {nums}")

print(nums)


## String sorting
s = "jklsIuL"
ls = list(s)
for i in range(len(ls)):
    min_index = i
    for j in range(i+1, len(ls)):
        if ls[j] < ls[min_index]:
            min_index = j
    ls[i], ls[min_index] = ls[min_index], ls[i]

print(''.join(ls))
        # min_ind

print("=========Printing sorted square=========")

def sqr_and_sort_inplace(lst):
    n = len(lst)
    start = 0
    end = len(lst) - 1
    position = 0
    result = [0] * n
    while start <= end:
        if abs(lst[start]) < abs(lst[end]):
            result[position] = lst[end] ** 2
            end -= 1
        else:
            result[position] = lst[start] ** 2
            start += 1
        position += 1
    return result


a = [-100,2,4,6,9]
print(f"sorted list is: {sqr_and_sort_inplace(a)}")