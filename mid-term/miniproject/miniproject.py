# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:07:53 2015

@author: whaochen
"""

import re
import time,sys
from selenium import webdriver
import urlparse 

#from selenium.webdriver.common.by import By





def parseJobList(driver,result,skill,key_word, job_company_file, job_skill_file):
    try:
        change_page=driver.find_element_by_link_text("Filter")
    except:
        print 'change page failed or no Filter'
        pass
    change_page.click()
    time.sleep(2)
    count=10
    while count>0:
        jobs= re.findall('data-li-position', driver.page_source)
        num=len(jobs)
        print num
        for i in range(num):
            try:
                xpath_style_Job="//ol[@id='results']/li[@class='mod result idx"+str(i)+" job']/a"
                job_detail_page=driver.find_element_by_xpath(xpath_style_Job)
                
                    
            except:
                error_type, error_obj, error_info = sys.exc_info()
                print 'get job detail failed'
                print error_type, 'Line:', error_info.tb_lineno
                sys.exit( 0 )
            try:
                job_detail_page.click()
            except:
                print "This list done"
                break
            count-=1 
            parseDetailPageRegex(driver, result, count,skill, key_word, job_company_file)
           
            
        try:
            next_page=driver.find_element_by_link_text("Next >")
        except:
            error_type, error_obj, error_info = sys.exc_info()
            print 'get job detail failed'
            print error_type, 'Line:', error_info.tb_lineno
            sys.exit( 0 )
        next_page.click()
        time.sleep(2)
    job_skill_file.write(key_word+': '+result)
    
    

def parseDetailPageRegex(driver, result, count, skill, key_word, job_company_file):
    company_name=re.search('job_view_topcard_company_name">[\w\W]*?<img class="logo" alt="(.*)" src=".*">[\w\W]*?</a>[\w\W]*?</div>', driver.page_source)    
    print "company name: "+company_name.group(1)
    job_company_file.write(company_name.group(1)+'  '+key_word+' '+'/n')
    applicants=re.search('<h3 class="applicant-count-number">(.*?)</h3>',driver.page_source)
    if applicants == None:
        driver.back()
    else:
        print "applicant: "+applicants.group(1)
        num_applicant=int(applicants.group(1))
        #job_description=re.search('<div class="description-module container">(.*)</div>[\w\W]*?<id="company-module">', driver.page_source)
        contentDiv = driver.find_element_by_css_selector('#layout-main > div > div.main > div.description-module.container > div')
        print contentDiv.text
        '(html|java|python|)'

        description=job_description.group(1).split()
        print description
        for word in description:
            if skill.has_key(word):
                skill[word] +=num_applicant
                result.add(word)
            else:
                continue
        
        
    print "already get page"+str(count)
    

skill={"Java":0,"C++":0,"python":0,"HTML":0,"JavaScript":0,
       "EC2":0,"Linux":0,"SQL":0,"bash":0,"VMware":0,
       "SAS":0,"Hadoop":0,"machine-learning":0,"C#":0,"Matlab":0,
       " R ":0, "visualization":0, "JQuery":0,"CSS":0,"TCP/IP":0}


Job_company_file= open('job_company','w')

Job_skill_file=open('job_skill', 'w')

skill_number_file=open('job_num','w')




base_url = "https://www.linkedin.com/uas/login"

driver =webdriver.Chrome('./chromedriver' )

driver.get(base_url)

time.sleep(2)
try:
    input_username=driver.find_element_by_name("session_key")
    input_username.send_keys("511688839@qq.com")
    input_password = driver.find_element_by_name("session_password")
    input_password.send_keys("bymyself1990")
except:
    error_type, error_obj, error_info = sys.exc_info()
    print 'fail to input '
    print error_type, 'Line:', error_info.tb_lineno
    sys.exit( 0 )

driver.add_cookie({'name':'session_key', 'value':'511688839@qq.com'})
driver.add_cookie({'name':'session_password','value':'bymyself1990'})

try:
    login=driver.find_element_by_name("signin")
except:
    error_type, error_obj, error_info = sys.exc_info()
    print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: home_page'
    print error_type, 'Line:', error_info.tb_lineno
    sys.exit( 0 )

time.sleep(1)
login.click()


time.sleep(2)

try:
    enter_search=driver.find_element_by_class_name("search-button")
except:
    error_type, error_obj, error_info = sys.exc_info()
    print 'enter_failed'
    print error_type, 'Line:', error_info.tb_lineno
    sys.exit( 0 ) 

time.sleep(1)
enter_search.click()


time.sleep(2)

vertical_links=re.findall('People</a></li><li><a href="(/vsearch.*)" data-li-vertical-type="jobs">Jobs</a>', driver.page_source)
#print driver.page_source
#print "-----------------------------------------------------------"
if len(vertical_links)>0:
    jobs_url=urlparse.urljoin(base_url,vertical_links[0])

    driver.get(jobs_url)
   
time.sleep(2)
'''
key_words=["software engineer","Business Analyst","system administrator","Database Administrator",
           "Network Engineer","data scientist","Data Engineer","Research Scientist","Full-stack developer"
           "Web Designer"]
'''
key_words=["software engineer"]
for key_word in key_words:
    result=[]
    try:
        input_keyworks=driver.find_element_by_id("advs-keywords")
        
        input_keyworks.send_keys(key_word)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'input keyword failed'
        print error_type, 'Line:', error_info.tb_lineno
        sys.exit( 0 ) 
    
    try:
        adv_search=driver.find_element_by_class_name("submit-advs")
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'search_failed'
        print error_type, 'Line:', error_info.tb_lineno
        sys.exit( 0 )
    
    adv_search.click()
    time.sleep(3)
    
    parseJobList(driver,result,skill,key_word,Job_company_file, Job_skill_file)    
    
skill_number_file.write(str(skill))

Job_company_file.close()
Job_skill_file.close()
skill_number_file.close()


print"..."


