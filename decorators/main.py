#!/usr/bin/env python
# encoding: utf-8

from functools import wraps


"""
Simple decorators
"""

def bread(func):
    def wrapper():
        print('/-----\\')
        func()
        print('\_____/')
    return wrapper


def ingredients(func):
    def wrapper():
        print('#tomato')
        func()
        print('~salad~')
    return wrapper


@bread
@ingredients
def sandwich(food='--ham--'):
    print food


"""
Passing arguments into a decorated function
"""

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print "Look what I've got:", arg1, arg2
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print "My name is", first_name, last_name


"""
Decorator maker
"""

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print "Я создаю декораторы! И я получил следующие аргументы:", decorator_arg1, decorator_arg2

    def my_decorator(func):
        print "Я - декоратор. И ты всё же смог передать мне эти аргументы:", decorator_arg1, decorator_arg2

        # Не перепутайте аргументы декораторов с аргументами функций!
        def wrapped(function_arg1, function_arg2) :
            print ("Я - обёртка вокруг декорируемой функции.\n"
                  "И я имею доступ ко всем аргументам: \n"
                  "\t- и декоратора: {0} {1}\n"
                  "\t- и функции: {2} {3}\n"
                  "Теперь я могу передать нужные аргументы дальше"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments("Леонард", "Шелдон")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
           " {1}".format(function_arg1, function_arg2))


"""
My test
"""

def my_decorator(a=None, b=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print('this is my_decorator')
            print("(a, b): (%s, %s)" % (a, b))
            #print("args: %s" % *args)
            #print("kwargs: %s" % **kwargs)
            f()
        return wrapper
    #return decorator if func is None else decorator(func)
    return decorator

@my_decorator(a=1, b='hello')
def foo():
    print('foo')


def print_separator():
    print('===================================')


def main():
    print_separator()
    sandwich()

    print_separator()
    print_full_name("Sam", "Smith")

    print_separator()
    decorated_function_with_arguments("Раджеш", "Говард")

    print_separator()
    foo()


if __name__ == '__main__':
    main()
