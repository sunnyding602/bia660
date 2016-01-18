
import re
import time,sys
from selenium import webdriver

def parseContent(driver):
    reviewList = driver.find_elements_by_class_name('review-text')
    starList = driver.find_elements_by_class_name('fk-stars')
    dateList = driver.find_elements_by_css_selector('div.date')

    reviewListTxt = []
    starListTxt = []
    dateListTxt = []
    for review in reviewList:
        reviewListTxt.append(review.text)
    
    for star in starList:
        starListTxt.append(star.get_attribute('title'))
    
    for date in  dateList:
        dateListTxt.append(date.text)

    return reviewListTxt, starListTxt, dateListTxt


#main url of the item
url1='http://www.flipkart.com/micromax-32b200hdi-81-cm-32-led-tv/product-reviews/ITMDTZ6NN78YHSZY'
url2 = 'http://www.flipkart.com/motorola-moto-360-smartwatch/product-reviews/ITME3VUPFFD9JGFD'
urls=[url1, url2]

for url in urls:
    print url
    #open the browser and visit the url
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    mergedReviewList = []
    mergedStarList = []
    mergedDateList = []
    page = 1
    while True:
        #sleep for 2 seconds
        time.sleep(2)
        reviewList, starList, dateList = parseContent(driver)
        mergedReviewList =  mergedReviewList + reviewList
        mergedStarList = mergedStarList + starList
        mergedDateList = mergedDateList + dateList
        try:
            cssPath = '#fk-mainbody-id > div > div.fk-review-page.gd-row.newvd > div.review-left.gd-col.gu12 > div.review-section.helpful-review-container > div.fk-navigation.fk-text-center.tmargin10 > a:nth-child(9)'
            if(page == 1):
                cssPath = '#fk-mainbody-id > div > div.fk-review-page.gd-row.newvd > div.review-left.gd-col.gu12 > div.review-section.helpful-review-container > div.fk-navigation.fk-text-center.tmargin10 > a.nav_bar_next_prev'
            nextBtn = driver.find_element_by_css_selector(cssPath)
            nextBtn.click()
        except:
            error_type, error_obj, error_info = sys.exc_info()
            print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
            print error_type, 'Line:', error_info.tb_lineno
            break
        page = page + 1
    
    fileWriter = open('out.txt','w')
    index = 0
    for review in mergedReviewList:
        fileWriter.write('xxx.com' + '\t'
                + mergedStarList[index].encode('ascii', 'ignore') + '\t' 
                + mergedDateList[index].encode('ascii', 'ignore') +'\t'
                + review.encode('ascii', 'ignore').replace('\n', '') + '\n' )
        index = index + 1


