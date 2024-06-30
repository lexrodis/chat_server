#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date

def main():
    """ Main program """
    print_date()
    return 0

def print_date():
    today = date.today()
    print(today)

if __name__ == "__main__":
    main()
