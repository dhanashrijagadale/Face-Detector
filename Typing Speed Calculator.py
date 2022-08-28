from time import *
import random as r

def mistake(paratest,user):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i]==user[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed(times,timee,user):
    timed=timee-times
    timer=round(timed,2)
    speed=(len(user)/timer)
    return round(speed,2)

test=["Artificial intelligence (AI) is the ability of a computer","or a robot controlled by a computer to do tasks that are usually done by humans",
      " because they require human intelligence and discernment"]
test1= r.choice(test)
print("Typing Speed Calculator")
print(test1)
print()
print()
time1=time()
testinput=input("Enter: ")
time2=time()

print("Speed",speed(time1,time2,testinput))
print("Mistake",mistake(test1,testinput))