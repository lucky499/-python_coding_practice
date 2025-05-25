# import datetime



# def add() -> int:
# 	return 5 + 4

# def subs() -> int:
# 	return 10 - 5

# def mult() -> int:
# 	return 10 * 5

# def main() -> None:
# 	print(type(add))
# 	addition: int = add()
# 	print(addition)
# 	# time.sleep(30)
# 	subtraction: int = subs()
# 	print(subtraction)
# 	# time.sleep(30)
# 	multiplication: int = mult()
# 	print(multiplication)
# 	# time.sleep(30)

# if __name__ == '__main__':
# 	main()


def outerfunc(func):
	print("outer")
	def innerfunc():
		print("inner")
		return func()
	return innerfunc()

print("super")
# @outerfunc
def name_func() -> int:
	print("hello Name")
	print(f"{100}")
	return 200

name_func = outerfunc(name_func)

def main() -> None:
	print("one")
	
	print("two")
	
	print(name_func)

if __name__ == '__main__':
	main()