# ## Fibonacci series
"""
from typing import Generator

def generate_fib() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main() -> None:     
    print(f"Enter number of fibonacci number limit")
    gen_object: Generator[int, None, None] = generate_fib()
    n = 10
    local_counter = 1
    while True:
        # input()
        for i in range(n):
            print(f"Fib number at place {local_counter} -> {next(gen_object)}")
            local_counter += 1
        print(f"Press Enter to next {n} of Fibonacci numbers: ")
        
        input()

if __name__ == "__main__":
    main()
"""


## Infinite loop of generator
"""
def infinite_repeater(lst):
    while True:
        for el in lst:
            yield el

repeater = infinite_repeater([1,2,3,4])

for _ in range(10):
    print(next(repeater))
"""