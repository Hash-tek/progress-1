print('Welcome to teasure island,\nYour mission is to find the treasure. ')
question=input('You meet yourself in front of two doors which one will you open,RIGHT/LEFT?\n  ').lower()
if question=='right':
    print("you were eaten by lions \nGAME OVER.")
else:
    next=input('You see two golden cups,one filled with milkthe other filled with water,which one will you choose,"milk" or "water"?\n').lower()
    if next =='milk':
        print('you will meet  a white angel that shows the way to heaven,\nYOU WIN!!!')
    else:
        print('you go to hell fire,\n PELE!!!!!') 
print("LAMIDI COPYRIGHT")