#!/usr/bin/env python3

from contextlib import contextmanager


'''
    The usual way of implementing a context manager
'''
class File(object):
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


'''
    Implementing a context manager as a generator
'''
@contextmanager
def open_file(name, method):
    f = open(name, method)
    yield f
    f.close()


def main():
    print('====================================')
    with File('blabla.txt', 'r') as foo:
        print('inside with statement')

    print('====================================')
    with open_file('blabla.txt', 'r') as foo:
        print('inside other with statement')


if __name__ == '__main__':
    main()
