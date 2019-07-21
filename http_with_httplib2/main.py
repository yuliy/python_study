#!/usr/bin/env python3

import httplib2
httplib2.debuglevel = 1


def main():
    h = httplib2.Http('.cache')
    response, content = h.request('http://lovioblaka.me')
    print( response.status )
    print( len(content) )
    #print( content.decode('utf-8') )


if __name__ == '__main__':
    main()
