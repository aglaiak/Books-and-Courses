# -*- coding: utf-8 -*-

hours=input("how many hours have you worked?")
rate=10 

def computepay(hours,rate):
 
  
    try:
         if float(hours)>40:
                    addhours=float(hours)-40
                    addpay=float(addhours)*1.5*10
                    pay=float(400 + (addpay))
                    print (pay)
         else:
                    pay=float(hours)*float(rate)
                    print (pay)
          
                               
    except: 
        print('Please enter numeric input') 
        

computepay(hours, rate)