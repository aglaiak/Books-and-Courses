# -*- coding: utf-8 -*-
score= input('Please enter your score')

try:

    if float(score) >=0 and float(score) <=1.0:
            if float(score) >= 0.9:
                print ('A')
            elif float(score) >= 0.8:
                print ('B')
            elif float(score) >=0.7:
                print ('C')
            elif float(score) >=0.6:
                print ('D')
            else:
                print ('F')
            
    else:
        print ("Bad score")
except: 
    print ("please enter a numerical value between 0 and 1")
    

