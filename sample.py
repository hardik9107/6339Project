import json
import csv

file = open("file1.csv","w")
a = csv.writer(file,dialect='excel')
row = ["user_id","business_id","stars"]
a.writerow(row)
with open("yelp_academic_dataset_review.json",'r') as data_file:            
    for line in data_file:
    #line = data_file.readline() 
        data = {}
        d = []
        data = json.loads(line)    
        d.append(data["user_id"])
        d.append(data["business_id"])
        d.append(data["stars"])
        a.writerow(d)
        print(d)
file.close()
