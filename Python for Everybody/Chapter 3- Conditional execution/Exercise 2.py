rate=10 

try:
      hours=float(input('How many hours you worked?'))
      if float(hours)>40:
             addhours=float(hours-40)
             addpay=float(addhours*1.5*10)
             pay=float((40*10)+addpay)
             print (pay)  
      else:
             print (hours*10)
except: 
        print('Please enter numeric input')     