import json
import pymongo
import csv
import pandas as pd
import matplotlib.pyplot as plt 
'''
client = pymongo.MongoClient("localhost",27017)
db = client["mikedb"]
mymoviecol = db["movie2"]
myquery = '{"numVotes":{"$gt":500}}'
with open('q41.csv', mode='w',newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["genre","avgRating"])
    for x in mymoviecol.find(json.loads(myquery)):
        #print(x["genres"])
        for y in x["genres"]:
            csv_writer.writerow([y,x["avgRating"]])
        #print(x["avgRating"])
'''            
q41data = pd.read_csv("q41-2.csv")        
print(q41data[["genre","avgRating"]].groupby("genre").describe())
plt.close("all")
q41data.boxplot(by = 'genre', column = ['avgRating'], grid=False, rot=-90, showfliers=False)
plt.title("Boxplot of Avg Rating for each genre")
plt.suptitle("")
#plt.set_xticklabels(q41data.index,rotation=90)
plt.show()

