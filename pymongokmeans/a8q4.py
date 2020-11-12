import json
import pymongo
import math
import matplotlib.pyplot as plt

def my_kmeans_iteration(mygenre, mykvalue):

    g = mygenre
    k = mykvalue
    numVotesThreshold = 10

    myclient = pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')

    db = myclient["mikedb"]
    mymoviecol = db["movie2"]
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
        }    
    ])

    sumofsquareerror = 0
    for x in myresult:
        #print("movie")
        #print(x["kmeansNorm"][0])
        #print(x["kmeansNorm"][1])
        iterK = 1
        kForMin = 1
        minDistanceSoFar = 100.0
        for y in mycentroidcol.find():
            #print("centroid")
            #print(y["kmeansNorm"][0])
            #print(y["kmeansNorm"][1])
            #print(str(y["_id"]) + " " + str(y["kmeansNorm"]))
            currCentroidDistance = math.sqrt((((float(y["kmeansNorm"][0]))-(float(x["kmeansNorm"][0])))**2)+(((float(y["kmeansNorm"][1]))-(float(x["kmeansNorm"][1])))**2))
            if(currCentroidDistance < minDistanceSoFar):
                minDistanceSoFar = currCentroidDistance
                kForMin = iterK
            iterK += 1
        oldCluster = 0
        try:
            oldCluster = int(x["cluster"])
        except:
            oldCluster = 0
        sumofsquareerror += (oldCluster-kForMin)**2
        mymoviecol.find_one_and_update({"_id": x["_id"]}, {"$set": {"cluster": kForMin}})

    #print("Sum of Square Error = " + str(sumofsquareerror))

    mycentroidcol = db["centroids"]
    mycentroidcol.drop()
    mycentroidcol = db["centroids"]

    for currK in range(k):
        currCentroid = currK + 1
        myresult = myclient['mikedb']['movie2'].aggregate([
            {
                '$match': {
                    'numVotes': {
                        '$gt': 10
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
                '$match': {
                    'cluster': currCentroid
                }
            }
        ]
        )
        numDocuments = 0
        sumStartYearNorm = 0.0
        sumAvgRatingNorm = 0.0
        for y in myresult:
            numDocuments += 1
            sumStartYearNorm += float(y["kmeansNorm"][0])
            sumAvgRatingNorm += float(y["kmeansNorm"][1])
        if(numDocuments > 0):
            post = {"_id" : currCentroid, "kmeansNorm" : [sumStartYearNorm/numDocuments, sumAvgRatingNorm/numDocuments]}
            mycentroidcol.insert_one(post)
        
        return sumofsquareerror
 
genresToTry = ["Action","Horror","Romance","Sci-Fi","Thriller"]
kMaxTimes = 100
kStart = 10
kEnd = 50
kStep = 5

myXArr = []
myYArr = []
for genreIter in genresToTry:
    #print(genreIter)
    currKVal = kStart
    myXArr = []
    myYArr = []
    numIterations = 0
    while currKVal <= kEnd:
        numIterations += 1
        #print(currKVal)
        errorNow = my_kmeans_iteration(genreIter, currKVal)
        myXArr.append(currKVal)
        myYArr.append(errorNow)
        if errorNow == 0:
            break
        if numIterations > kMaxTimes:
            break
        currKVal += kStep
    plt.plot(myXArr, myYArr)
    plt.xlabel('k')
    plt.ylabel('square error')
    plt.title("Sum of Square Errors vs k for Genre = "+genreIter)
    plt.show()    
    getUserEnter = input("Press Enter to continue...")
