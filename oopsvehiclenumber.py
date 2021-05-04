import json
import random
import string


class Vehicle:


    def returnvehiclenumber(self,statename,location):
        with open('numberplatedata.json', 'r') as json_file:
            data = json.load(json_file)
            for i in data["states"]:
                if (i["state_name"] == statename):
                    statecode = i["Group_of_letters"]
                    rtocode = i["location"][location]

        randomstr = []
        for i in range(0, 2):
            randomstr.append((random.choice(string.ascii_uppercase)))

        randomnum = []
        for i in range(0, 4):
            randomnum.append((random.randint(0, 9)))

        print(statecode + " " + rtocode + " " + ''.join(randomstr) + " " + ''.join(map(str, randomnum)))


    def adddata(self, newstatename, newstatecode, location):


        def write_json(data, filename='numberplatedata.json'):
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

        newelement = {
            "state_name": newstatename,
            "Group_of_letters": newstatecode,
            "location": location
        }

        with open('numberplatedata.json', 'r+') as json_file:
            data = json.load(json_file)
            temp = data['states']
            temp.append(newelement)
            write_json(data)
            print("Data Added")

    def removedata(self, dstatename):
        def write_json(data, filename='numberplatedata.json'):
            with open(filename, 'r+') as file:
                json.dump(data, file, indent=4)

        with open('numberplatedata.json', 'r+') as json_file:
            data = json.load(json_file)
            for i in data["states"]:

                if (i["state_name"] == dstatename):

                    temp = data["states"]
                    temp.remove(i)
                    write_json(data)
                    print("Data Deleted")

    def update(self, statename, statecode, location):

        def write_json(data, filename='numberplatedata.json'):
            with open(filename, 'r+') as file:
                json.dump(data, file, indent=4)

        jsonfile = open('numberplatedata.json', )
        jsondata = json.load(jsonfile)

        for i in jsondata["states"]:
            if (i["state_name"] == statename):
                i['Group_of_letters'] = statecode
                i['location'] = location
                write_json(jsondata)
                print("Data Updated")


