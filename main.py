#!/usr/bin/env python
# -*- coding: utf-8 -*-
from print_date import print_date, print_nice_date 
from user_input import user_numbers

def main():
    """ Main program """
    print_date()
    print_nice_date()
    user_numbers(input("Enter some numbers seperated by blank space: \n"))




if __name__ == "__main__":
    main()
