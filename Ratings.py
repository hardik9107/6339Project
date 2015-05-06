import json
import math


users = {}
business = {}
b_avg = {}
similar = {}

#calculating user-user similarity using Pearsons correlation similarity
def user_similarity(allusers,user1,user2):
    sim = {}
    for business in allusers[user1].keys():
        if business in allusers[user2].keys():
            sim[business] = 1
    size = len(sim)
    if(size == 0):
        return 0
    sum_user1 = 0
    sum_user1_sq = 0
    sum_user2=0
    sum_user2_sq = 0
    prod_user1_user2 = 0
    for business in sim:
        sum_user1 += int(allusers[user1][business])        
        sum_user2 += int(allusers[user2][business])
        sum_user1_sq += pow(int(allusers[user1][business]),2)
        sum_user2_sq += pow(int(allusers[user2][business]),2)
        prod_user1_user2 += ((int(allusers[user1][business]) * int(allusers[user2][business])))
    numerator = (prod_user1_user2)-((sum_user1 * sum_user2)/size)
    denominator = math.sqrt(((sum_user1_sq - pow(sum_user1,2))/size)*((sum_user2_sq - pow(sum_user2,2))/size))
    if denominator == 0:        
        return 0
    res = numerator/denominator
    return res

#Finding the top 50 users that are similar to the test user
def topMatches(users,user):    
    similar = {}
    similar[user] = {}
    for user_a in users.keys():
        if user_a == user:
            continue
        similar[user][user_a] = user_similarity(users,user,user_a)
    sc = [(score,user1) for user1,score in similar[user].items()]       
    sc.sort()
    sc.reverse()    
    return sc[0:50]

#Calculating the rating that the test user might give to the test business
def calcRatings(users,user,sc,business):
    user_avg = 0
    for buss in users[user]:
        user_avg += int(users[user][buss])
    user_avg = user_avg/len(users[user])
    sim_usr_avg = {}
    for sim_scr,usr in sc:
        avg = 0
        for buss in users[usr]:
            avg += int(users[usr][buss])
        avg = avg/len(users[usr])
        sim_usr_avg[usr]=avg
    sum_prod = 0
    sum1 = 0
    for sim_scr,usr in sc:
        if business not in users[usr].keys():            
            prod = (sim_scr) * (b_avg[business] - sim_usr_avg[usr])
        else:
            prod = (sim_scr) * (int(users[usr][business]) - sim_usr_avg[usr])
        sum_prod += prod
        sum1 = sum1 + sim_scr
    print(user_avg)
    print(sum_prod)
    print(sum1)
    try:
        div = sum_prod/sum1
    except ZeroDivisionError:
        div = 0
    return (user_avg + div)

def main(user,test_business):
    with open("UserRatings.json",'r') as data_file:
        users = json.load(data_file)
    if(test_business not in users[user].keys()):
        with open("Businesses.json",'r') as business_file1:
            b1 = json.load(business_file1)
            for k in b1.keys():
                sum_b = 0
                for k1 in b1[k].keys():
                    sum_b += int(b1[k][k1])
                avrg = (sum_b/len(b1[k]))
                b_avg[k] = avrg
        sc = topMatches(users,user)
        rating = calcRatings(users,user,sc,test_business)
        return rating
    else:
        return users[user][test_business]
        
#main('3n9nr9635rImbN7SAQ0EWw','TI00GrtJIH5A5qXhpq025g')   