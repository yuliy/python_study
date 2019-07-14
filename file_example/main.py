#!/usr/bin/env python3


def main():
    line_number = 0
    with open('sample.txt', encoding='utf-8') as f:
        for line in f:
            line_number += 1
            print('{:>4}| {}'.format(line_number, line.rstrip()))


if __name__ == '__main__':
    main()
