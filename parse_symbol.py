# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:22:34 2022

@author: Xun.Zheng
"""
import re
ERROR_CODE = {
    "InVaild_Format":"Wrong expression",
    "Out_Of_Range":"Ipunt is out of Range",
    "Start_Greater_End":"Start time should smaller than end time"
              }

reg = {
       "dash":"([0-9]+[\-][0-9]+)",
       "comma":"([0-9]+([\,][0-9]+)+)",
       "star":"(\*)",
       "slash":"((([0-9]+)|(\*))[\/][0-9]+)",
       "num":"([0-9]+)"
       }

def is_InVaild(pattern, string):
    res = re.match(pattern, string)  
    if res and res.group() == string:
        return False
    else:
        return True
    
def is_OutOfRange(string, scope):
     if string[0] < scope[0] or string[1]> scope[1]:
        return True
     else:
        return False

def parse_dash(string, scope): 
    if is_InVaild(reg["dash"], string):
        return "InVaild_Format"

    string =  [int(n) for n in string.split("-")]
    
    if is_OutOfRange(string, scope):
        return "Out_Of_Range"
    if string[0] > string[1]:
        return "Start_Greater_End" 
    
    res = []
    for i in range(string[0], string[-1] + 1):
        res.append(i)
    return res
        
def parse_comma(string,scope): 
    if is_InVaild(reg["comma"], string):
        return "InVaild_Format"
    string = [int(n) for n in string.split(",")]
  
    res = []
    for i in string:
        if i < scope[0] or i > scope[1]:
            return "Out_Of_Range"
        res.append(i)
    return res

def parse_slash(string, scope): 
    if is_InVaild(reg["slash"], string):
        return "InVaild_Format"
    string = string.replace("*", str(scope[0])) 
    string = [int(n) for n in string.split("/")]
    
    if is_OutOfRange(string, scope): 
        return "Out_Of_Range"
    
    start = string[0]
    add = string[1]      
    end = scope[1]
    res = []
    while start <= end:
        res.append(start)
        start = start + add
    return res
 
def parse_star(string, scope): 
    if is_InVaild(reg["star"], string):
        return "InVaild_Format"
    res = []
    for i in range(scope[0], scope[1] + 1):
        res.append(i)
    return res

def parse_num(string, scope): 
    if is_InVaild(reg["num"], string):
        return "InVaild_Format"
    num = int(string)
    if num < scope[0] or num > scope[1]:
        return "Out_Of_Range"
    else:
        return [num]