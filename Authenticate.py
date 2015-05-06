import json

def main(username,password):
    with open("authentication.json",'r') as data_file:             
        data = json.load(data_file)
        if(data[username] == password):
            return 1
        else:
            return 0 

print(main('JmrWw7R6W1i-vz-VPG25Kw','Aysia'))