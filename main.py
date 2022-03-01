# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 21:54:47 2022

@author: Xun.Zheng
"""


import os
import sys
import parse_symbol as ps

    
def handle_field(string, scope):
    if "-" in string:
        res = ps.parse_dash(string, scope)
    elif "," in string:
        res = ps.parse_comma(string, scope)
    elif "/" in string:
        res = ps.parse_slash(string, scope)
    elif "*" in string:
        res = ps.parse_star(string, scope)
    else:
        res = ps.parse_num(string, scope)
    return res


def handle_minute(string):
    scope = [0,59]
    res = handle_field(string, scope)
    return res

def handle_hour(string):
    scope = [0,23]
    res = handle_field(string, scope)
    return res

def handle_day(string):
    scope = [1,31]
    res = handle_field(string, scope)
    return res

def handle_month(string):
    scope = [1,12]
    res = handle_field(string, scope)
    return res

def handle_weekday(string):
    scope = [1,7]
    res = handle_field(string, scope)
    return res

def handle_res(time_field, time_name):
    if isinstance(time_field, str):  
        print("{} Error".format(time_name),"   ",ps.ERROR_CODE[time_field])
        sys.exit() 


def parse_cron_string(line):
    print(line)
    line = line.split()
    if len(line) != 6:
        print("Number of Field Error")
        return
    
    minute = handle_minute(line[0])
    handle_res(minute, "Minute Field")
    
    hour = handle_hour(line[1])
    handle_res(hour, "Hour Field")
    
    day_of_month = handle_day(line[2])
    handle_res(day_of_month, "Day Field")
       
    month = handle_month(line[3])
    handle_res(month, "Month Field")
    
    day_of_week = handle_weekday(line[4])
    handle_res(day_of_week, "Weekday Field")
    
    command = line[5]
    
    print("%-14s" % "minute", ' '.join([str(n) for n in minute]))
    print("%-14s" % "hour", ' '.join([str(n) for n in hour]))
    print("%-14s" % "day_of_month", ' '.join([str(n) for n in day_of_month]))
    print("%-14s" % "month", ' '.join([str(n) for n in month]))
    print("%-14s" % "day_of_week", ' '.join([str(n) for n in day_of_week]))
    print("%-14s" % "command", command)



'''
string = "*/15 0 1,15 * 1-5 /usr/bin/find"
parse_cron_string(string)
'''

if __name__ == '__main__':
    parse_cron_string(sys.argv[1])
    os.system('pause')

