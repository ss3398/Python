import json
import pymongo

g = "Short"
k = 5
numVotesThreshold = 10

myclient = pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')

db = myclient["mikedb"]
mymoviecol = db["movie2"]
mycentroidcol = db["centroids"]
mycentroidcol.drop()
mycentroidcol = db["centroids"]

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
                '$gte': 1800
            }
        }
    }, {
        '$match': {
            'avgRating': {
                '$gte': 0
            }
        }
    }, {
        '$match': {
            'genres': g
        }
    }, {
        '$sample': {
            'size': k
        }
    }
])

iterK = 1
for x in myresult:
    post = {"_id" : iterK, "kmeansNorm" : x["kmeansNorm"]}
    mycentroidcol.insert_one(post)
    iterK += 1
    