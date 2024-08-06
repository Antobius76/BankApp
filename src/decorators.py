def log(filename=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error.")
                else:
                    print(f"{func.__name__} error: {e}. Inputs {args}, {kwargs}.")
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
