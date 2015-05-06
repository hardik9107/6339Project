import json
import csv
import math
import random


users = {}
business = {}
b_avg = {}
similar = {}

#finding the similarity between two businesses
def business_similarity(business,business1,business2):
    sim = {}
    for parameter in business[business1].keys():
        if (parameter == 'categories') | (parameter == 'neighborhoods') | (parameter == 'hours'):
            count = 0
            for category in business[business1][parameter]:
                if category in business[business2][parameter]:
                    count += 1
            if (len(business[business1][parameter]) == 0):
                if (len(business[business2][parameter]) > 0):
                    sim[parameter] = 0
                else:
                    sim[parameter] = 1
            else:
                sim[parameter] = count/len(business[business1][parameter])
            continue
        if (parameter == 'city')| (parameter == 'review_count') | (parameter == 'type') | (parameter == 'stars') | (parameter == 'open') | (parameter == 'state'):
            if business[business1][parameter] == business[business2][parameter]:
                sim[parameter] = 1
    size = len(sim)
    total = 0
    for parameter in sim.keys():
        total += sim[parameter]
    res = total/size            
    return res

#Finding similarity between the businesses that the user has reviewed with other businesses
def find_similarity(business,user,business1):
    similar = {}
    similar[business1] = {}
    for business2 in business.keys():
        if business2 == business1:
            continue
        similar[business1][business2] = business_similarity(business,business1,business2)
    sc = [(score,business_a) for business_a,score in similar[business1].items()]       
    sc.sort()
    sc.reverse()                             
    return sc[0:10]

def main(input_user):
    with open("UserRatings.json",'r') as data_file:
        users = json.load(data_file)     
        
    with open("Businesses3.json",'r') as business_file:
        business = json.load(business_file)
    count = 0
    sim_business = {}
    for user in users.keys():        
        if user == input_user:
            #print(user)
            if user not in sim_business.keys():
                sim_business[user] = {}
            for business1 in users[user].keys():
                if (business1 not in  sim_business[user].keys()):
                    sim_business[user][business1] = {}
                sim_business[user][business1] = find_similarity(business,user,business1)
                print(sim_business[user][business1])
    sim = []
    for business1 in users[input_user].keys():
        for score, simbusiness in sim_business[input_user][business1]:
            if(simbusiness not in sim):
                sim.append(simbusiness)
    count = 0
    disp_sim = []            
    while(count < 10) :
        id = random.randrange(len(sim))
        disp_sim.append(sim[id])
        count += 1                  
    print(disp_sim)
    return


#main('7xdvRGaz6fIG6Uh4vPTe2g')