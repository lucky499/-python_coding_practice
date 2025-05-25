def is_palindrome(pal_string: str) -> bool:
    if type(pal_string) is not str:
        return 0
    if len(pal_string) == 0:
        return 0
    left: int = 0 
    right: int = len(pal_string) - 1
    while left < right:
        if pal_string[left] != pal_string[right]:
            return False
        left += 1
        right -= 1
    return True

pal_string: str = "racecar"
is_pal: bool = is_palindrome(pal_string)
if is_pal:
    print(f"the string: {pal_string} is a palindrome")
else:
    print(f"the string: {pal_string} is not a palindrome")