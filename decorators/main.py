#!/usr/bin/env python


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


def main():
    sandwich()

if __name__ == '__main__':
    main()
