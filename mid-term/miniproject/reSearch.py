# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:07:53 2015

@author: whaochen
"""

import re

#f = open('data')
#content = f.read()
#f.close()
#applicants=re.search('<h3 class="applicant-count-number">(.*?)</h3>',content)
#print applicants


f = open('jd')
content = f.read()
f.close()

job_description=re.search('<div class="description-module container">(.*)</div>[\w\W]*?<id="company-module">', content)
print job_description
