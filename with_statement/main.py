#!/usr/bin/env python3

class Foo(object):
    def __init__(self, file_name, method):
        print('__init__')
        self.file_obj = open(file_name, method)

    def __enter__(self):
        '''Here we should return some closable object'''
        print('__enter__')
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print('__exit__')
        self.file_obj.close()


def main():
    with Foo('blabla.txt', 'r') as foo:
        print('inside with statement')


if __name__ == '__main__':
    main()
