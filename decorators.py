## Decorators
def logging_method(fun):
    def attendance():
        print(f"The name shared is")
        return fun("Lxm")
    return attendance()


def main() -> None:
    @logging_method
    def attnd(name):
        print(f"Hello :{name}")


if __name__ == "__main__":
    main()


