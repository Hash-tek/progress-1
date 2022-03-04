print('welcome to sally ice cream stand')
bill=0
Type = input('what type of ice cream do you want? s,m,l?\n').lower()
if Type =='s':
    bill=5
    print('it will cost $5')
elif Type =='m':
    bill=8
    print('it will cost you $8')
else:
    bill=12
    print('it will cost you $12')
sprinkle = input('do you want to add sprinkle? Y/N').upper()
if sprinkle =='Y':
    add_sprinkle = input('do you want strawberry or vanilla sprinkle? S/V ').upper()
    if add_sprinkle == 'S':
        bill+=2
        print('it will cost you additional $2')
    else:
        bill+=1
        print('it will cost you additional $1')
else:
    print(f'your fee is ${bill} ')
print(f'your bill is ${bill}')
print('Thanks for the patronage')

