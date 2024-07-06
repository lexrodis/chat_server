#!/usr/bin/env python
# -*- coding: utf-8 -*-
from print_date import print_date, print_nice_date 
from user_input import user_numbers, user_numbers_min, user_numbers_max

def main():
    """ Main program """
    print_date()
    print_nice_date()

    numbers_string = input("Enter some numbers seperated by blank space: \n")
    result = user_numbers(numbers_string)
    print("You entered {}".format(result))
    smallest_number = user_numbers_min(numbers_string)
    print("The smallest number is {}".format(smallest_number))

    biggest_number = user_numbers_max(numbers_string)
    print ("The Biggest number is {}".format(biggest_number))




if __name__ == "__main__":
    main()
