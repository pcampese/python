#!/usr/bin/env python
"""Testing out python arguments."""

import argparse

def main():
    """This is the main function."""

    parser = argparse.ArgumentParser(description='My Sample Description.')
    parser.add_argument('-f', '--filename',
                        required=True)
    parser.add_argument('-w', '--wizard_mode',
                        choices=['Master', 'Apprentice'],
                        default='Master')
    parser.add_argument('integers',
                        metavar='N',
                        type=int,
                        nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum',
                        dest='accumulate',
                        action='store_const',
                        const=sum,
                        default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)

if __name__ == "__main__":
    main()
