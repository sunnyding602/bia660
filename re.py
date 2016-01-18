import re
str = 'from 1 to 10'
result = re.findall('(from\s?\d+\s?to\s?\d+)',str )
print result
