import pprint
laptop = [{'brand':'lenovo','color':'grey','os':'windows'}]
print(pprint.pformat(laptop))
fileobj = open('mylaptop.py','w')
fileobj.write('laptop = '+ pprint.pformat(laptop)+'\n')
fileobj.close()