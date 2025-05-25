# from typing import List

# def longestCommonPrefix(strs: List[str]) -> str:
#     string_len = len(strs) - 1
#     combined_string = ','.join(strs)
#     prefix = ''

#     for l in combined_string:
#         # prefix = prefix + l
#         print(f"insdie: {prefix}")
#         if l == ',':
#             break
#         else:
#             if combined_string.count(f',{prefix + l}') == string_len:
#                 prefix = prefix + l
#             else:
#                 if len(prefix) >= 1:
#                     return prefix
#                 return f""
#     # return prefix

# pref = longestCommonPrefix(["flower","flow","flight"])
# print(pref)
                    

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""        
        if strs == [""]:
            return prefix
        if len(strs) == 1:
            return strs[0]
        # if 
        string_len = len(strs) - 1
        combined_string = ','.join(strs)
        # print(f"combined string: {combined_string}")
        # print
        for l in combined_string:
            if l == ',':
                break
            else:
                if combined_string.count(f',{prefix + l}') == string_len:
                    prefix = prefix + l
                else:
                    if len(prefix) >= 1:
                        return (prefix)
                    prefix = ""
                    return prefix

pref = Solution().longestCommonPrefix(eval(input()))
print(pref)
                    
