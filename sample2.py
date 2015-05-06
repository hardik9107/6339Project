import json
import csv

users = {}
business = {}
file = open("UserRatings1.json","w")
#writer = csv.writer(file)
file1 = open("Businesses1.json","w")
#writer = csv.writer(file)
with open("file2.csv",'r') as data_file:
    lines = csv.reader(data_file)
    next(lines,None)          
    for line in data_file:                 
        if(line == '\n'):
            continue
        a = line.split(',')    
        if(a[0] not in users.keys()):
            users[a[0]] = {}        
        s = a[2].split('\n')
        users[a[0]][a[1]] = s[0]
        if(a[1] not in business.keys()):
            business[a[1]]={}
        business[a[1]][a[0]] = s[0]        
json.dump(users,file)        
json.dump(business,file1)            
file.close()
file1.close()