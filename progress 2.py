#BMI
height=float(input('enter your height in m: '))
weight=float(input('enter your weight in kg '))
#print (type(height))
bmi=(weight / height **2)
print (bmi)
if bmi <=0.0034:
    print('you are underweight')
elif bmi <= 0.0035:
     print("you are overweight")    
else:
    print('obesity!!!!!')     