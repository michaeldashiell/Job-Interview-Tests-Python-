# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:41:59 2020

@author: Michael
"""
### 
count = 0
while count < 100:
    count = count + 1
    if count % 15 == 0:
        print('fizzbuzz')
    elif count % 3 == 0:
        print('fizz')
    elif count % 5 == 0:
        print('buzz')
    else:
        print(count)
    
