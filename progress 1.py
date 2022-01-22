print('WELCOME TO THE ROLLERCOSTER')
height=int(input('what is your height? '))
bill=0
if height >120:
    age=int(input('what is your age? '))
    if age <= 18:
        bill=5
        print('aldolescent ticket are $5')
    elif age <= 25:
        bill=6
        print ( 'youth ticket are $6 ')    
    else:
        bill=7
        print(' adult ticket are $7') 
    photo=input('do you want a photo? Y/N')
    if photo =='Y':
      bill+=3
    print(f'your bill is {bill}')
else:
    sorry=int(input('your age?'))
    if sorry<= 10:
        print('have an ice cream')
    else:
         print ("go home")
    print('grow taller')
print('BYE!!!')         
