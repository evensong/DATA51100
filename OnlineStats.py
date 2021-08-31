# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:31:31 2021

Ben Haws
DATA 51100 Fall 2021
OnlineStats--Wk1 programming assignment
"""
def main():

    intro = '''DATA-51100, Fall 2021
Name: Ben Haws
Programming Assignment #1'''
    
    print(intro)

    userIn = 0
    count = 0 #keep track of user variables entered as if in list

    mean = 0
    prevMean = 0 #keep track of previous mean for variance calculation
    variance = 0

    while userIn >= 0:
        print("Enter a number:", end = ' ')
        try:
            userIn = float(input())
            
            if userIn < 0: #don't print/calc mean and variance when negative number entered
                break
            
            count += 1 
            
            #online algorithm to find mean
            prevMean = mean
            mean += (userIn - mean) / count
            
            #online algorithm to find
            #if statement prevents dividing by zero on first case
            if count == 1:
                variance = 0 #variance of a single element is always 0
                
            else:
                variance = ((count - 2) / (count - 1)) * variance + (userIn - prevMean)**2 / count
            
            print('Mean is ' + str(mean) + ' variance is ' + str(variance) + '\n')
            
        except ValueError: #if the user enters a non-numeric value
            print('Please enter a numeric value') 
    return

if __name__ == '__main__':
    main()