#!/usr/bin/env python3

import xml.etree.ElementTree as etree


def main():
    tree = etree.parse('sample.xml')
    root = tree.getroot()
    print(root)


if __name__ == '__main__':
    main()
