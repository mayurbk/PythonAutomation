import threading, time
print('start of program')

#create function
def takebreak():
    time.sleep(3)
    print("Start OFF !!!")
    

threadObj = threading.Thread(target=takebreak)

threadObj.start()
print('END OF PROGRAM.')

