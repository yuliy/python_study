#!/usr/bin/env python

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
Decorators with parameters
"""

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print "Look what I've got:", arg1, arg2
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print "My name is", first_name, last_name


def main():
    sandwich()
    print_full_name("Sam", "Smith")

if __name__ == '__main__':
    main()
