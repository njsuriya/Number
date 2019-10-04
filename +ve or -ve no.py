while True:
    
 try:
  a=int(input('Enter the Number:'))
  break
  
 except:
  print("Please enter a NUMBER!")

if a>0:
 print('POSITIVE')
 
elif a==0:
 print('ZERO')
 
else:
 print('NEGATIVE')
 
