# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:11:59 2015

@author: yangjie
"""

import re
import string
#import urllib2

fileReader = open('data.txt')
fileWriter = open('out.txt','w')
def inNormalRange(num):
    if(string.atof(num) >=0 and string.atof(num) <=17):
        return True
    else:
        return False

for line in fileReader:
    
    orig_line = line.strip()
    line = re.sub('\d+ pound', '', line)
    line = re.sub('\d+\.\d+ pound', '', line)
    line = re.sub('\d+ month', '', line)
    founditer = re.finditer('(\d+)\s?to\s?(\d+)', line)
    founditer2 = re.finditer('(\d+\.\d+)\s?to\s?(\d+\.\d+)', line)
    
    num_str = ''
    for it in founditer:
        if(False ==inNormalRange(it.group(1))):
            break
        if(False ==inNormalRange(it.group(2))):
            break
        num_str = it.group(0)

    for it in founditer2:
        if(False ==inNormalRange(it.group(1))):
            break
        if(False ==inNormalRange(it.group(2))):
            break
        num_str = it.group(0)



    if num_str == '': 
        words = line.split()
        num_str = ''
        
        for word in words:
            try:
                num = string.atof(word)
                if(num >=0 and num <=17):
                    num_str = num_str +" "+ str(num)
            except ValueError:
                ''
        print orig_line + '\t'+num_str
    else:
        print orig_line + '\t' +num_str

fileReader.close()
fileWriter.close()
