# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
#core modules
import datetime
from datetime import date 
import time 
from time import time 

#today = datetime.date.today()
today = date.today()
timestamp = time.time()
print(timestamp)


# use pip to install modules

# see whats installed pip3 freeze


#pip module 
import camelcase 
from camelcase import CamelCase 

c = Camelcase()
print(c.hump('hello there world'))

# custom module to import 

import validator 
from validator import validate_email

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
        print('email is bad')