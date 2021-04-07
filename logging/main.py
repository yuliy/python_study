#!/usr/bin/env python
# encoding: utf-8

import logging
#logging.setLevel(logging.DEBUG)
logging.basicConfig(filename='example.log', level=logging.DEBUG)

def main():
    logging.debug('my debug message')
    logging.error('my error message')
    logging.info('my info message')


if __name__ == '__main__':
    main()
