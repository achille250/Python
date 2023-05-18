# python data type
# determine your data datatype

c=True
print (type(c))

# Working with strings
print('my name is cesar')
# adding variables
law=('Happy birthday to my love')
print(len(law))

# checking string
law=('Happy birthday to my love')
print ('birthday' in law)

#Upper and lower case 
law=('Happy Birthday To my love')
print (law.lower())

#concatenation
a='beautiful'
b='day'
c= a+" "+b
print (c)

#list
students=['cesar','Joseph','Gladys','Prince',"Kael"]
print (students)

# accessing list items
students=['cesar','Joseph','Gladys','Prince',"Kael"]
print (students[-2])

# ranges of indexes
students=['cesar','Joseph','Gladys','Prince',"Kael","Pazo","NIC",'Ben']
print (students [2:5])
print (students [:5])

#change list items
students=['cesar','Joseph','Gladys','Prince',"Kael","Pazo","NIC",'Ben']
students [6]="george"
print (students)

# insert into list
students=['cesar','Joseph','Gladys','Prince',"Kael","Pazo","NIC",'Ben']
students.insert(2,'Nelson')
print(students)

# appending to list

students=['cesar','Joseph','Gladys','Prince',"Kael","Pazo","NIC",'Ben']
students.append('Festus')
print(students)

#remove items from list
students=['cesar','Joseph','Gladys','Prince',"Kael","Pazo","NIC",'Ben']
students.remove('Joseph')
students.remove(2)
print(students)
