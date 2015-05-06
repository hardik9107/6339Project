import json
import csv

business = {}
file1 = open("Businesses2.json","w")
#writer = csv.writer(file)
with open("yelp_academic_dataset_business.json",'r') as data_file:                 
    for line in data_file:                 
        data = {}
        d = {}
        data = json.loads(line) 
        #print(data)
        if data["business_id"] not in business.keys():
            business[data["business_id"]] = {}
            business[data["business_id"]]['categories'] = data['categories']
with open("file1.csv",'r') as csv_data_file:
    lines = csv.reader(csv_data_file)
    next(lines,None)          
    for line in csv_data_file:                 
        if(line == '\n'):
            continue
        a = line.split(',')                    
        s = a[2].split('\n')
        if(a[1] not in business.keys()):
            business[a[1]]={}
        business[a[1]][a[0]] = s[0]       
json.dump(business,file1)            
file1.close()