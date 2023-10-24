#!/usr/bin/env python3
''' template for date assignment script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
Program: a1_M_keshavarz.py (replace M_keshavarz with your student name)
Author: "M_keshavarz"
The python code in this file (a1_M_keshavarz.py) is original work written by
"M_keshavarz". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource.
'''
import os
import sys

def leap_year(obj):
    '''
    *******************************
    return a year is leap or not. 
        parameters:               
            obj-int:year              
        return:                   
            status-boolean: true or false 
    *******************************
    '''
    status= False
    if ((obj %4==0 and obj %100!=0)or(obj %400==0)):
        status = True

    return status

def sanitize(obj1,obj2):
    '''
    *********************************************************************
    remove all of non digit char in the input string.                  
        parameters:                                                    
            obj1-str:input string                                          
            obj2-str:allow characters                                      
        return:                                                        
            results-str:a string equal digit input with keeping the order  
    *********************************************************************
    '''
    results=''
    for char in obj1:
        if char in obj2:
            results+=char
    
    return results

def size_check(obj, intobj):
    '''
    *********************************************************************
    Check if the length of the input string matches the expected length.

    Parameters:
        obj-str: input string
        intobj-int: expected length

    Returns:
        status-boolean: True if the length matches, False otherwise
    *********************************************************************   
    '''
    status=False
    if len(obj)== intobj:
        status=True

    return status

def range_check(obj1, obj2):
    '''
    *********************************************************************
    Check if the input value (obj1) is within the specified range (obj2).

    Parameters:
        obj1-int: input value
        obj2-int: tuple representing the range (min, max)

    Returns:
        status-boolean: True if obj1 is within the range, False otherwise
    *********************************************************************   
    '''
    status=False
    low, high=obj2
    if low <= obj1 and obj1 <= high:
        status=True

    return status
    
def usage():    
    '''
    *********************************************************************
    Display a usage message when user enter incorrect number of arguments.

    Returns:
        message-str: A string containing the message.
    *********************************************************************
    '''
    status="Usage: a1_M_Keshavarz.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   #print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)  
