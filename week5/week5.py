import re,sys,urllib2,os,time

fileReader=open('in.txt')
fileWriter=open('out.txt', 'w')
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

countOfAugReviews = 0 #total count of auguest reviews
for line in fileReader: 
    link=line.strip() 

    pageNumber = 1
    while True:
        openLink = link + '?pageNumber='+str(pageNumber) 
        try:
            #use the browser to get the url.
            print 'reading ' + openLink
            response=browser.open(openLink)    
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            print 'ERROR FOR LINK:',openLink
            print error_type, 'Line:', error_info.tb_lineno
            continue
        
        html=response.read()    

        indexOfEnd = html.find('<span class="a-size-medium">Sorry, no reviews match your current selections.</span>')
        if(indexOfEnd >= 0):
            break

        ignoreTwo = 0
        if(html.find('<h4 class="a-size-medium view-point-title">Most helpful positive review</h4>') >= 0):
            ignoreTwo = 2

        dateIter=re.finditer('<span class="a-size-base a-color-secondary review-date">(.*?)</span>', html)#get all the matches

    
    
        for date in dateIter:
            if(ignoreTwo > 0):
                ignoreTwo = ignoreTwo -1
                continue
            dateFound = date.group(1)
            print dateFound
            dateFound = dateFound.lower()
            #august
            if(dateFound.find('august') >=0):
                print dateFound, 'found~~~~!!'
                countOfAugReviews = countOfAugReviews+1

        time.sleep(3)
        pageNumber = pageNumber + 1

print 'countOfAugReviews:', str(countOfAugReviews) 
fileWriter.write(str(countOfAugReviews))
fileWriter.close()
fileReader.close()
