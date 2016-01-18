#import the two libraries we will be using in this script
import urllib2,re,sys
import operator

with open('./in.html', 'r') as content_file:
    content = content_file.read()

usersDict = dict()
users=re.finditer('<div class="htmlxquoteauthor">(.*?) wrote: </div>',content)#get all the matches

for user in users:
    username=user.group(1) # get the username
    #username = username.lower().strip()
    username = username.strip()
    if (username in usersDict):
        usersDict[username] = usersDict[username] + 1
    else:
        usersDict[username] = 1



sortedDict = sorted(usersDict.items(), key=operator.itemgetter(0))

for key, value in sortedDict:
    print key, value
