print('calculate BMI\n')

h = float(input('Enter User Hight m :'))
w = float(input('Enter User weight kg : '))

bmi = w / (h**2)
print("your bmi :",bmi)
if bmi < 18:
    print('you are underweighted')
elif (bmi >= 18 and bmi < 22 ):
    print(f'BMI = is {bmi} you are healthy.')
elif (bmi >= 22 and bmi < 25):
    print(f'BMI = is {bmi} you are overweighted.')
elif (bmi >=25 and bmi <30 ):
    print(f'BMI = is {bmi} you are overweighted.')
else:
    print("enter correct value")