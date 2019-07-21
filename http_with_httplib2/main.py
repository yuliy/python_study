#!/usr/bin/env python3

import httplib2


def main():
    h = httplib2.Http('.cache')
    response, content = h.request('http://yuliy.me')
    print( response.status )
    print( len(content) )


if __name__ == '__main__':
    main()
