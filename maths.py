from calculator import addding, subtracting, multiplying

if __name__ == "__main__":
    a: int = 10
    b: int = 5
    summ = addding(a, b)
    subt = subtracting(a, b)
    multi = multiplying(a, b)
    print(f"sum: {summ}")
    print(f"subtracting: {subt}")
    print(f"multiplying: {multi}")