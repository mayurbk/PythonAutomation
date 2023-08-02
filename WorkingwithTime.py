import time
print(time.time())     ###EPOCH time is that from when a programming language borns/starts.12 am on Jan1 1970

def cal():
    product = 1
    for i in range(1,999):
        product = product*i

    return product
starttime = time.time()
result = cal()

endtime = time.time()

print('the result is %s digits long' %(len(str(result))))
print("The calculation took %s seconds" %(endtime-starttime))


#use of sleep
# for i in range(5):
#     print("tic")
#     time.sleep(1)
#     print('tok')
#     time.sleep(1)
#
#
# time.sleep(5)

