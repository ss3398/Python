# Requires the PyMongo package.
# https://api.mongodb.com/python/current
import json
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
numVotesThreshold = 10

db = myclient["mikedb"]
mymoviecol = db["movie2"]

myresult = myclient['mikedb']['movie2'].aggregate([
    {
        '$match': {
            'numVotes': {
                '$gt': numVotesThreshold
            }
        }
    }, {
        '$match': {
            'type': 'movie'
        }
    }, {
        '$match': {
            'startYear': {
                '$gt': 1800
            }
        }
    }, {
        '$match': {
            'avgRating': {
                '$gte': 0.0
            }
        }
    }
])

minStartYear = 3000
maxStartYear = 1800
minAvgRating = 10.0
maxAvgRating = 0.0

for x in myresult:
    #print("avgRating = "+ str((x["avgRating"]).to_decimal()))
    if(int(x["startYear"]) < minStartYear):
        minStartYear = int(x["startYear"])
    if(int(x["startYear"]) > maxStartYear):
        maxStartYear = int(x["startYear"])
    if(float(x["avgRating"]) < minAvgRating):
        minAvgRating = float(x["avgRating"])
    if(float(x["avgRating"]) > maxAvgRating):
        maxAvgRating = float(x["avgRating"])
    #print("trying to update "+ str(x["_id"]))
    #mymoviecol.find_one_and_update({"_id": x["_id"]}, {"$set": {"kmeansNorm": [str(x["startYear"]),str(x["avgRating"])]}})


print("max avg rating = "+str(maxAvgRating))
print("min avg rating = "+str(minAvgRating))
print("max start Year = "+str(maxStartYear))
print("min start Year = "+str(minStartYear))

myresult = myclient['mikedb']['movie2'].aggregate([
    {
        '$match': {
            'numVotes': {
                '$gt': numVotesThreshold
            }
        }
    }, {
        '$match': {
            'type': 'movie'
        }
    }, {
        '$match': {
            'startYear': {
                '$gt': 1800
            }
        }
    }, {
        '$match': {
            'avgRating': {
                '$gte': 0.0
            }
        }
    }
])

for x in myresult:
    currStartYear = int(x["startYear"])
    scaledStartYear = ((currStartYear - minStartYear)*1.0)/(maxStartYear - minStartYear)
    currAvgRating = float(x["avgRating"])
    scaledAvgRating = (currAvgRating - minAvgRating)/(maxAvgRating - minAvgRating)
    mymoviecol.find_one_and_update({"_id": x["_id"]}, {"$set": {"kmeansNorm": [str(scaledStartYear),str(scaledAvgRating)]}})
    