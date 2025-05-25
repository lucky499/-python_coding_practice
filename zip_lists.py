from itertools import zip_longest

def sum_equal_lists(l1, l2) -> None:
    sum_list = [a + b for a, b in zip(l1, l2)]
    print(sum_list)

def sum_inequal_lists(l1, l2, l3) -> None:
    sum_list = [a + b + c for a, b, c in zip_longest(l1, l2, l3, fillvalue=0)]
    print(sum_list)

def main() -> None:
    sum_equal_lists([2,5], [5,6])
    sum_inequal_lists([2,5], [5,6,10], [9,6])

if __name__ == "__main__":
    main()