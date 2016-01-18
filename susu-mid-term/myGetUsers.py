
#import the two libraries we will be using in this script
import urllib2,re,sys,json,time
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('utf8')

browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]


pagesToGet=2
for page in range(0,pagesToGet):
    
    print 'processing page :', page
    
    url='http://s.club.jd.com/productpage/p-1510479-s-0-t-3-p-'+ str(page) +'.html'

    try:
        #use the browser to get the url.
        response=browser.open(url)    
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print 'ERROR FOR LINK:',url
        print error_type, 'Line:', error_info.tb_lineno
        continue
    
    myHTML=response.read()

    print myHTML
    jsonObj = json.loads(myHTML)
    print jsonObj

