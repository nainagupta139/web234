print('Enter time')
print('----------')
h1=int(input('Enter hours - '))
m1=int(input('Enter minutes - '))
x=str(input('Enter AM or PM - '))
if(x=='PM' or x=='pm'):
    h1=h1+12
count=0
if(h1>0 and h1<12):
    if(m1>=0 and m1<60):
        if(x=='AM' or x=='PM' or x=='pm' or x=='am' ):
            print('The time is',h1,':',m1)
            count=1
if(count==0):
    print('Please enter time correctlty')
