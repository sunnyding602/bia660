# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:16:10 2015

@author: yangjie
"""


import re,sys
import time
import urllib2



fileReader = open('in.txt')
fileWriter1 = open('bestbuyReviewText.txt','w')
fileWriter2 = open('bestbuyReviewTime.txt','w')
fileWriter3 = open('bestbuyReviewStar.txt','w')


browser=urllib2.build_opener()


browser.addheaders=[('User-agent', 'Mozilla/5.0')]


url='http://www.flipkart.com/micromax-32b200hdi-81-cm-32-led-tv/product-reviews/ITMDTZ6NN78YHSZY?pid=TVSDTZ6NN78YHSZY&rating=1,2,3,4,5&reviewers=all&type=top&sort=most_helpful&start='+start 
for line in fileReader:
    Num_Reviews = line.strip()
    NumberPage = 1
    while True:
        ReviewLink = Num_Reviews + '?pageNumber='+str(NumberPage)
        NumberPage += 1
        try:
            response=browser.open(ReviewLink) 
            print ReviewLink
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            print 'ERROR FOR LINK:',ReviewLink
            print error_type, 'Line:', error_info.tb_lineno
            continue

        time.sleep(3)
    
        myHTML = response.read()
        indexOfEnd = myHTML.find('<span class="a-size-medium">Sorry, no reviews match your current selections.</span>')
        if(indexOfEnd >= 0):
            break
        #print myHTML        
        
        allusers=set()
        ReviewLines = re.finditer('<span class="BVRRReviewText">(.*?)</span>', myHTML)
        for ReviewLine in ReviewLines:
            ReviewText = ReviewLine.group(1)
            fileWriter1.write(str(ReviewText))           
           
            
        ReviewDates= re.finditer('<span class="BVRRValue BVRRReviewDate">(.*?)</span>',myHTML)
        for ReviewDate in ReviewDates:
            ReviewTime = ReviewDate.group(1)
            fileWriter2.write(str(ReviewTime))
            
            
        ReviewStars = re.finditer('<span class="BVRRNumber BVRRRatingNumber">(.*?)</span>',myHTML)
        for ReviewStar in ReviewStars:
            ReviewLevel = ReviewStar.group(1)
            fileWriter3.write(str(ReviewLevel))
             
    
fileReader.close()
fileWriter1.close()
fileWriter2.close()
fileWriter3.close()
