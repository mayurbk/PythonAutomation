import datetime
# print(datetime.datetime.now())
#
# dt = datetime.datetime(2023,8,10,12,15,14)  ##YYYY MM DD   Time HH:MM:SS
# print(dt)
#
# #working with time delta
#
# delta = datetime.timedelta(days= 10, hours= 11, minutes= 5, seconds=10)
# print(delta.days)

#adding number of days from current
dt  = datetime.datetime.now()
print(dt)
proposedtime = datetime.timedelta(days=10)
print(dt+proposedtime)

#converting date time into string objects
date = datetime.datetime(2023,10,28,14,30,40)
print(date.strftime('%Y/%m/%d %H:%M:%S'))

print(date.strftime('%I:%M:%a'))
