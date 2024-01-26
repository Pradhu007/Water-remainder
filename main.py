import time
import pyttsx3
# pip3 install pyttsx3

def ismidnight():
    current_time = time.localtime()

    if current_time.tm_hour == 0 and current_time.tm_min == 0 and current_time.tm_sec == 0:
        return True
    else:
        return False

targettime = int(input("Enter the time in seconds"))
timetogetwaterback = int(input("Time to get drink water and come back to computer?. think of the worst case scenario"))

start_time = time.time()
while(ismidnight() != True):
    elapsedtime = time.time() - start_time

    if(elapsedtime >=  targettime):
        engine = pyttsx3.init()
        engine.say("GO AND DRINK YOUR WATER NOW BRO!")
        engine.runAndWait()
        print("Waiting for user to come back")
        time.sleep(timetogetwaterback) # wait for user to come back
        start_time = time.time()
    else:
        continue
