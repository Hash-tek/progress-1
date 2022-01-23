print('welcome to sally pizza')
bill=0
order=input('what size pizza do you want? S,M,L:  ').upper()
if order == 'S':
    bill = 15
    print ('it will cost you $15')
elif order =='M':
    bill=20
    print ('it will cost you $20')
else:
    bill =25
    print ('it will cost you $25')
add_cheese=input('do you want cheese? Y OR N: ').upper()
if add_cheese=='Y':
    bill+=1
    print ('added')
add_pepperoni=input('do you want pepperoni? S OR ML: ').upper()
if add_pepperoni == "S":
    bill+=2
    print('it will cost you $2')
else:
    bill+=3
    print ('it will cost you $3') 
print (f'your bills is ${bill}')              


