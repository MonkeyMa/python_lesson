#!/usr/local/lib/python2.7
# -*- coding: utf-8 -*-

"""
# Copyright (C) 2008-2017 ***
# Comments: learn argparse lib
# Author  : MonkeyMa
# Changes : 1) create the file 2017-11-04
"""

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)
