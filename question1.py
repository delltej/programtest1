a=int(input(" Enter the month in the numeric form "))
b=int(input(" Enter the day in numeric form "))
c=int(input(" Enter the year as two numerical digits "))
d=1
if a > 0 and a<=12:
    d=1
else:
    d=0
if b > 0 and b<=31:
    d=1
else:
    d=0
if c >0 and c<=99:
    d=1
else:
    d=0

if d ==0:
    print("invalid")   
else: 
    print("Success: Congratulations! you entered the correct date.")
    print("the date is",a,"/",b,"/",c)

