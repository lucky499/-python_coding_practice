def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

genn_object = my_generator()
gen_obj = iter(my_generator())   
print(next(gen_obj))   
print(next(genn_object))   
print(next(gen_obj))   
print(next(genn_object))   
print(next(gen_obj))   
print(next(genn_object))   
# print(next(gen_obj))   
# print(next(gen_obj))   
# print(next(gen_obj))   
# print(next(gen_obj))
# print(iter(gen_obj))
# for val in my_generator():
#     print(val)