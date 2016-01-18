
import re
import time,sys
import urllib2
from selenium import webdriver


#main url of the item
url='https://www.kaggle.com/competitions'

#open the browser and visit the url
myDict = dict()
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
#sleep for 2 seconds
time.sleep(2)
cssPath = '#all-switch'
btn = driver.find_element_by_css_selector(cssPath)
btn.click()

time.sleep(2)
checkBoxCssPath = '#completed'
cbBtn = driver.find_element_by_css_selector(checkBoxCssPath)
cbBtn.click()
time.sleep(2)

table = driver.find_element_by_id('competitions-all')
myHtml = table.get_attribute('innerHTML')
hrefs=re.finditer('<a href="(.*?)">',myHtml)
for href in hrefs:
    if '/competitions' not in href.group(1):
        myDict[href.group(1)] = href.group(1)
#print myDict, len(myDict)

for request_target in myDict:
    if '//' in request_target:
        continue
    url = 'https://www.kaggle.com'+request_target #desc
    url_price = url+'/details/prizes'

    filename = request_target.replace('/c/', '')
    urlfile=urllib2.urlopen(url)
    html=urlfile.read()
    fw=open('yo'+filename+'.html','w')
    fw.write(html)
    fw.close()


