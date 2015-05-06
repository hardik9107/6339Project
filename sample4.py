import json
import csv

business = {}
file1 = open("Businesses3.json","w")
#writer = csv.writer(file)
with open("yelp_academic_dataset_business.json",'r') as data_file:                 
    for line in data_file:                 
        data = {}
        d = {}
        data = json.loads(line) 
        print(data.keys())
        if data["business_id"] not in business.keys():
            business[data["business_id"]] = {}
        for key in data.keys():
            if (key == 'business_id') | (key == 'full_address') | (key == 'name') | (key == 'latitude') | (key == 'longitude'):
                continue
            business[data["business_id"]][key] = data[key]       
json.dump(business,file1)            
file1.close()