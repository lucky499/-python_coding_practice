class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = list(str(x))
        # is_pal = True
        start = 0
        end = len(sx) - 1
        while start < end:
            if sx[start] != sx[end]:
                return False
            start += 1
            end -= 1
        return True

print(Solution().isPalindrome(121213))