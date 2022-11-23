import base64
import json

MainURL = input("Input the main url \n")
ConfigDecoded = json.loads(base64.b64decode(MainURL[8:]))

UUids = ["e7a54616-4cc0-41c4-a325-2b57b10fb572", "f670b53f-16ab-410c-a10a-a36268c26491", "7007628f-da9a-4d47-984e-5d5193b78911","0e4ae5cf-a324-47e7-88aa-1fca2dfa6cfd","c4a11233-b7e4-4151-ac0e-312bca3fcaf1", "40c2d7d7-a490-49a2-830e-6923770a70e7","810ac0fd-7f94-4a06-bc60-79c9e6b9d198"]

f = open("NewUserLinks.txt", "w")

for uuid in UUids:
    ConfigDecoded["id"] = uuid
    ConfigDecoded["ps"] = uuid + " @vpn_unblock"
    NewConfigDecoded =  str(json.dumps(ConfigDecoded))
    NewUrl= "vmess://" + str(base64.b64encode(NewConfigDecoded.encode('utf-8')))[2:-1] + "\n\n"
    print(NewUrl)
    f.write(NewUrl)
    
f.close()
input()
