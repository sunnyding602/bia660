import re,sys,urllib2,os,time
html = 't-count"><h3 class="applicant-count-number">15</h3><p class="applicant-text">Applicants</p></div><div class="'
dateIter=re.finditer('<h3 class="applicant-count-number">(.*?)</h3>', html)#get all the matches
for x in dateIter:
    print x.group(1)

    
