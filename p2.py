import json
import pymongo

client = pymongo.MongoClient("localhost",27017)
db = client["mikedb"]
mymoviecol = db["movie2"]
myextradatacol = db["extradata2"]

mymoviedoc = mymoviecol.find()
movieCount = 0
matchCount = 0
moreThanOnematchCount = 0

for x in mymoviedoc:
    movieCount += 1
    #print(x["titleLabel"])
    #movietitle = x["titleLabel"]["value"]
    #print(x["title"])
    myquery = '{"titleLabel" : {"type":"literal","value":"' + x["title"]+'"}}'
    #print(myquery)
    currentMatchCount = 0
    for y in myextradatacol.find(json.loads(myquery)):
        matchCount += 1
        currentMatchCount += 1
    if currentMatchCount > 1:
        moreThanOnematchCount += 1
print(str(movieCount) + " documents found in the movie collection. "+str(matchCount) + " matches found. "+str(moreThanOnematchCount) + " cases where multiple matches on title found.")

