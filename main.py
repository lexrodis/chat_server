#!/usr/bin/env python
# -*- coding: utf-8 -*-
from print_date import print_date, print_nice_date 
from user_input import UserNumbers

def main():
    """ Main program """
    print_date()
    #print_nice_date()

    numbers = UserNumbers(input("Enter some numbers seperated by blank space: \n"))
    print("You entered {}".format(numbers.numbers))
    print("The smallest number is {}".format(numbers.min()))
    print ("The Biggest number is {}".format(numbers.max()))


    f = open('output.txt', 'w')
    f.write(f'The result is {numbers.numbers}\n')
    f.write(f'The smallest is {numbers.min(=)}\n')
    f.write(f'The biggest number is {numbers.max()}\n')


    f.close()




if __name__ == "__main__":
    main()
