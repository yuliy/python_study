#!/usr/bin/env python3

import httplib2
httplib2.debuglevel = 1


def print_response(response, content):
    print( F'status: {response.status}' )
    print( F'content len: {len(content)}' )
    print( F'cached: {response.fromcache}' )


def main():
    h = httplib2.Http('.cache')

    # response 1
    print( '_____________________________________' )
    response, content = h.request('http://lovioblaka.me')
    print_response(response, content)

    # response 2
    print( '_____________________________________' )
    response, content = h.request('http://lovioblaka.me')
    print_response(response, content)

    # response 3
    print( '_____________________________________' )
    response, content = h.request('http://lovioblaka.me',
        headers={'cache-control': 'no-cache'})
    print_response(response, content)


if __name__ == '__main__':
    main()
