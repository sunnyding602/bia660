
import re
import time,sys
from selenium import webdriver

def parseContent(driver):
    reviewList = driver.find_elements_by_class_name('desc')
    dateList = driver.find_elements_by_class_name('time')
    starList = driver.find_elements_by_css_selector('div.grade-star')

    reviewListTxt = []
    starListTxt = []
    dateListTxt = []
    for review in reviewList:
        reviewListTxt.append(review.text)
    
    for star in starList:
        starListTxt.append(star.get_attribute('class'))
    
    for date in  dateList:
        dateListTxt.append(date.text)

    return reviewListTxt, starListTxt, dateListTxt


#main url of the item
#url='http://www.flipkart.com/micromax-32b200hdi-81-cm-32-led-tv/product-reviews/ITMDTZ6NN78YHSZY'
#url = 'http://www.flipkart.com/motorola-moto-360-smartwatch/product-reviews/ITME3VUPFFD9JGFD'

url = 'http://item.jd.com/1413830.html?jd_pop=1720e106-bae3-40c5-a542-01a2f916b398&abt=0#comment'
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
    if(page == 2):
        break;
    reviewList, starList, dateList = parseContent(driver)
    mergedReviewList =  mergedReviewList + reviewList
    mergedStarList = mergedStarList + starList
    mergedDateList = mergedDateList + dateList
    try:
        cssPath = '#comment-0 > div.com-table-footer > div > div > a.ui-pager-next'
        nextBtn = driver.find_element_by_css_selector(cssPath)
        nextBtn.click()
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break
    page = page + 1

for x in mergedReviewList:
    print x
