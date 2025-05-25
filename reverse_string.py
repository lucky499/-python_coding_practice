def reverse_the_string(rev_string: str) -> str:
    return rev_string[::-1]

def reverse_string_function(rev_string: str) -> str:
    if type(rev_string) is not str or len(rev_string) == 0:
        return "Not a valid string"
    else:
        rev_string = list(rev_string)
    left: int = 0
    right: int = len(rev_string) - 1
    while left < right:
        rev_string[left], rev_string[right] = rev_string[right], rev_string[left]
        left += 1
        right -= 1
    return ''.join(rev_string)

rev_strng: str = "abcdefgh"
print(f"Reversed string is: {reverse_the_string(rev_strng)}")
print(f"Reversed string is: {reverse_string_function(rev_strng)}")
