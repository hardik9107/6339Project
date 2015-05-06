import json


file = open("authentication.json","w")
with open("yelp_academic_dataset_user.json",'r') as data_file:            
    data = {}
    d = {}    
    for line in data_file:
    #line = data_file.readline() 
        
        data = json.loads(line)    
        d[data["user_id"]] = data["name"]
json.dump(d,file)               
file.close()
