#!/usr/bin/env python3


from http.client import HTTPConnection
from urllib.request import urlopen


HTTPConnection.debuglevel = 1


def main():
    response = urlopen('http://yuliy.me')
    print( response.headers.as_string() )


if __name__ == '__main__':
    main()
