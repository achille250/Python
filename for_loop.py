students=['Amos','Gladys','Nelson','Farouk']
for x in students:
    print(x)
for x in 'Lawrence':
    print(x)
#the break statement
students=['Amos','Gladys','Nelson','Farouk']
for x in students:
    print(x)
    if x=='Gladys':
        break
students=['Amos','Gladys','Nelson','Farouk']
for x in students:
    if x=='Gladys':
        continue
    print(x)
#the range function
for x in range(6):
    print(x)
#the range function
for x in range(2,6):
    print(x)
#nested loop

adj=['fair','beautiful','handsome']
students=['Rafique','Abena','Prince']
for x in adj:
    for y in students:
        print (x,y)