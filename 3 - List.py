#creation of a list
my_list=["apple","banana","orange",105,-234] #creation of a list
#print the list
print (my_list)

#In the following way we ask python to take the string at index [0]
#and pick the character at index [2]
print ((my_list[0])[2])

#In the following way we ask python to take the string at index [0]
#and pick the character at index [3]
print ((my_list[0])[3]) 

#CHALLENGE:create a loop that print out only float from the list
#counter to be use as a index value
a=-1
#i will take the same value of the value picked from the list
for i in my_list:
    a+= 1
    #with this function we check if the value is a float
    def check(i):
        try:
            float(i)
            return True
        except ValueError:
            return False
    #if the value is a float we print it    
    if check(i) == True:
        print (my_list[a])

