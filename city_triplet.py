# import requests
# import mysql.connector
# import pandas as pd

s = """Jamie,city1,4                   
Dana,city1,3                  
Jamie,city2,1
Jamie,city3,3
Dana,city3,2
Jamie,city4,2
Dana,city4,1"""

records = s.split("\n")
data = []
for r in records:
    data.append(r.strip().split(","))

d = {}
for record in data:
    try:
        name = record[0] 
        if name in d.keys():
            d[name].append([record[1],record[2]])
        else:
            d[name] = [[record[1],record[2]]]
    except Exception as e:
        print("re:",record)

#print(d)
#Sort Values for each key in d

def create_triplets(l):
    if len(l) < 3:
        return 
    result = []
    for i in range(0,len(l)-2):
        triplet = []
        triplet.append(l[i][0])
        triplet.append(l[i+1][0])
        triplet.append(l[i+2][0])
        result.append(triplet)
    return result
        

from itertools import combinations
d2 = {}
for k,v in d.items():
    l = sorted(v,key=lambda x: x[1])
    print(k,l)
    combi =  create_triplets(l)
    print("combi:",combi)
    for c in combi:
        c = ";".join(c)
        if c not in d2.keys():
            d2[c] = 1
        else:
            d2[c]+=1
        
print(d2) # at task partition level


    






    
    





