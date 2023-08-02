#Key - Value pair
mycat = {'size':'fat','color':'white','age':2}  #key and values

StudentDetails = dict()
StudentDetails[1] = 'arrav'
StudentDetails[2]= 'bassi'
StudentDetails[3]='christopher'
print(StudentDetails)
print(StudentDetails[2])
print(mycat['color'])

##Write a dictionary to enter bdays of 4 people and extract any value from it.
bday = {"Alice":'April 2',"Bob":'Jan 3',"Chris":'March 4','tony':'Dec 3'}

while True:
    print('enter your name or q to quit')
    name = input()
    if name =='q':
        break

    if name in bday: #alice checks for key
        print(bday[name] + ' is your birthdate.') #bday[alice]

    else:
        print('no birthday information .Enter your bday.')
        bdate = input()
        bday[name] = bdate
        print('Your birthday is update.')
        print(bday)

#get() method.
Items = {'Apples': 5, "Eggs": 10, "Cups": 10,"Biscuit":15}
print("We have "+ str(Items.get('Eggs')) + ' apples for sale.')

counts = dict()
print ('Enter a line of text:')
line = input('')
words = line.split()  # hellow, world
print ('Words:', words)
print ('Counting...')

for i in words: #i is hello
    counts[i] = counts.get(i,0) + 1
print( 'Counts', counts)


