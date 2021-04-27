import json
import random
import string

jsonfile = open('vehicledata.json', )
jsondata = json.load(jsonfile)

state = input("Enter the name of your state")
location = input("Enter your location")

for i in jsondata["states"]:
    if(i["state_name"]==state):
        statecode = i["Group_of_letters"]
        rtocode = i["Location"][location]

        
randomstr = []
for i in range(0, 2):
    randomstr.append((random.choice(string.ascii_uppercase)))

    
randomnum = []
for i in range(0, 4):
        randomnum.append((random.randint(0, 9)))
        


print(statecode + " " + rtocode + " " + ''.join(randomstr)+ " " + ''.join(map(str,randomnum)))
jsonfile.close()
