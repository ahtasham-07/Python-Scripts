#t1 = Cold Water Temperature
#t2 = Hot Water Temperature
#x = Required Temperature taken from user
#m1 = Mass taken from Cold water
#m2 = Mass taken from Hot water

#DATA
t1 = 20 #Taken from Cold Glass temperature sensor
t2 = 100 #Taken from Hot Glass temperature sensor
center_point = ((t2-t1)/2)+t1
x = int(input('Enter Required Temperature: ')) 

#Result
if x>t1 and x<t2:
    if x<center_point:
        print('m1 : m2 = 1 :', (x-t1)/(t2-x)) 
    elif x>=center_point:
        print('m1 : m2 =',(t2-x)/(x-t1), ' : 1')
elif x==t1 or x==t2:
    print('There is no need to mix!')
else:
    print('Required Temperture is out of range!')