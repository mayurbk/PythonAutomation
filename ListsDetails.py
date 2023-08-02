#ordered sequence - INDEX
list1 = ['cat','dog','birds',80,90, True,21,12,42,45]
print(list1[-2])    #negative index starts from -1 wrt Right end

##slicing of list
print(list1[2:])
print(len(list1))

##mutable - can we change/alter items in list - list is mutable
list1[2]='newValue'
print(list1)
list1[4]=list1[1]
print(list1)

##list concatenation replication
x=list1+['new','very new','most recent']
print(x)
print(list1*2)

#remove items from list
print(list1.pop(3)) ## works with index
print(list1.remove(21)) ## works with value
list1.append('addingValue')
print(list1)
list1.insert(3,'addthis')
print(list1)