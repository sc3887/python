import time
#ex1
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time
    return wrapper


@calculate_time
def func(num):
    for i in range(1, num):
        print(i)


print(func(15))


#ex2
def cashe(func):
    cashe_dict = {}
    def wrapper(num):
        if num in cashe_dict:
            return cashe_dict[num]
        result = func(num)
        cashe_dict[num] = result
        return  result

    return wrapper


@calculate_time
@cashe
def fib1(num):
    if num <= 1:
        return num
    return fib1(num - 1) + fib1(num - 2)


@calculate_time
def fib2(num):
    if num <= 1:
        return num
    return fib2(num - 1) + fib2(num - 2)


print(fib1(14))
print(fib2(14))

#https://github.com/sc3887/python.git