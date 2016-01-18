import re,sys,urllib2,os




fileReader=open('in.txt')

fileWriter=open('out.txt', 'w')
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

for line in fileReader: 
    username=line.strip() 
    profileLink = 'https://www.freelancer.com/u/'+username+'.html'
    try:
        #use the browser to get the url.
        print 'reading ' + profileLink
        response=browser.open(profileLink)    
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print 'ERROR FOR LINK:',link
        print error_type, 'Line:', error_info.tb_lineno
        continue
    
    html=response.read()    

    #taglines=re.finditer('profile.saveByline">(.*?)<', html, re.S)#get all the matches
    taglines=re.finditer('tagline":"(.*?)"', html)#get all the matches
    

    taglines=re.finditer('<li>\S+<div class="review"(.*?)</div>\S+</li>', html, re.S)#get all the matches
    
    for tagline in taglines:
        taglineText=tagline.group(1) # get the username
        fileWriter.write(taglineText.strip()+'\n')
        print taglineText.strip()

fileWriter.close()
fileReader.close()
