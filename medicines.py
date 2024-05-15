from pymongo import MongoClient
import time

CONNECTION_STRING = "mongodb://localhost:27017/MediBuddy"
client = MongoClient(CONNECTION_STRING)
db = client['MediBuddy']
print(''' Have to take
        Tacrolimus: 1 time (till 23-11-2022)
        Optive: 1 time (till 23-11-2022)
        Patadine : 1 time (till 23-11-2022)
        Slit: 1 time(Before dinner, Keep in mouth for 10mins) \n''')
meds = ['Tacrolimus','Optive','Patadine','slit']
total= [1,1,1,1]
def print_times():
    a = []
    flagged = []
    i = 0
    for l in db['medicines'].find():
        print(f"{meds[i]}  : {l['times']}")
        if(l['times']==total[i]):
            print(f'you are done for the day for {meds[i]}')
            flagged.append(meds[i])
        a.append(l['times'])
        i = i+1
    if(len(flagged)==4):
        print('ALL DONE FOR TODAY')
        time.sleep(3)
        exit()
    return [a,flagged]
def update():
    m= print_times()
    #print(m)
    a = m[0]
    flagged = m[1]
    i = 0
    while(i<4):
        if(meds[i] in flagged):
            pass
        else:
            x = int(input(f"enter times {meds[i]} taken since last time :"))
            if(x>0):
                query =  {"Medicine_name" : meds[i]}
                val = {"$set" : {"times" : x+a[i]}}
                #print(query)
                db['medicines'].update_one(query,val)
        i = i+1
    print_times()
    time.sleep(10)

def wipeout():
    for l in db['medicines'].find():
        query = {"Medicine_name": l["Medicine_name"]}
        val = {"$set":{"times":0}}
        db['medicines'].update_one(query,val)
        

day = int(input("Is it a new day? PRESS 0 FOR NO AND 1 FOR YES: "))
if(day==1):
    wipeout()
    update()
else:
    update()


client.close()




