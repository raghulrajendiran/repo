print (': Simple Interest :\n')	

def Simple_Interest():
    rate = input('Enter rate percentage')
    principle = input('Enter the principle amount')
    x = input('Select \'1\' for duration of time in days  \n\'2\' for time in months and \n\'3\' for time in years')
    principle = float(principle)
    if(x == 1):
        time = input('Enter number of days')
        time = time /(12*30)
    elif(x == 2):        
        time = input('Enter number of months')
        time = time / 12
    else:
        time = input(' Enter number of years')

    simple_Interest = ( principle * rate * time ) / 100
    print(' Simple Interest = %f ' %simple_Interest)

    total = principle + simple_Interest
    print(' Total amount = %f ' %total )
