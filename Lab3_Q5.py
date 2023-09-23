def repeat(re):
    def my_decorator(func):
        def wrapper(*numbers):
            for i in range(re):
                func(*numbers)
        return wrapper
    return my_decorator

x = int(input("Enter a number of repetitions: "))

@repeat(x)
def hello():
    print('Hello')

hello()