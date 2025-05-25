from typing import Dict
from collections import Counter

def club_dicts(d1, d2) -> Dict:
    return d1.update(d2)

def summ_dicts(d1, d2) -> Dict:
    return dict(Counter(d1) + Counter(d2))


def main() -> None:
    d1 = {'a': 1, 'b': 5}
    d2 = {'a': 31, 'n': 55}
    print(f"clubbed dict is: {club_dicts(d1, d2)}")
    print(f"clubbed dict is: {summ_dicts(d1, d2)}")



if __name__ == "__main__":
    main()