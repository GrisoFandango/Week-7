a="hello, world"

#with this method you replace a letter
a=a.replace("h","H") 
print (a)

a="hello, world"
#you make capital the first letter
a=a.capitalize() 
print (a)

a="hello, world"
#In this way the all string become capital
a=a.upper() 
print(a)

a="hello, world"
#In this way is possible to choose which
#letters to capitalize
a=((a[0]).upper() 
   +(a[1:7])
   +a[7].upper()
   +(a[8:]))
print(a)
