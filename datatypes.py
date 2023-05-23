# Working with tuples

fruits=("orange","mango","banana","sweer apple","Kiwi","cherry","water mellon")
print (type(fruits))

#accessing your tuple

fruits=("orange","mango","banana","sweer apple","Kiwi","cherry","water mellon")
print (fruits[3:5])


#fruits=("orange","mango","banana","sweer apple","Kiwi","cherry","water mellon")
#fruits.insert(2,'strawbery')
#print (fruits)

#add to tuples
fruits=("orange","mango","banana","sweer apple","Kiwi","cherry","water mellon")
#fruits.insert(2,'strawbery')
y=list(fruits)
y.append('strawberry')
fruits=tuple(y)
print (fruits)

#dictionaries
student = {"name":"Cesar",
           "Country":"Rwanda",
           "Sex":"Male",
           "City":"Kigali"}
print(student)

#accessing your dictionary

student = {"name":"Cesar",
           "Country":"Rwanda",
           "Sex":"Male",
           "City":"Kigali"}
print(student["Country"])

#Update dictionaries

student = {"name":"Cesar",
           "Country":"Rwanda",
           "Sex":"Male",
           "City":"Kigali"}
student.update({'City':'Gikondo'})
print(student)

#conditional statement
#If statement

a=33
b=200

if b > a :
    print("B is grater than a")
    
    #elif statement
    a=33
    b=33
    if b>a:
        print("b is grater than a")
    elif a==b:
        print ('a and b are equal')
    
    #else statement
    a=200
    b=33
    if b>a:
        print('b is grater than a')
    elif a==b:
        print('a and b are equal')
    else:
        print('a is greater than b')
        
        #else without elif statement
        
        a=200
        b=33
        if b>a:
            print("b is greater than a")
        else:
            print ("a is greater than b")
    #add keyword
    a=200
    b=33
    c=500
    if a>b and c>a:
        print('both condition are true')
        
        #or statement
        a=200
        b=33
        c=500
        if a>b or a>c:
         print("at least one of the condition is true")
            