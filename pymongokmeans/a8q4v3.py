import json
import pymongo
import math
import matplotlib.pyplot as plt

from files.aq8q2f import myq2

def dist_between_points(p11,p12,p21,p22):
    return math.sqrt(((p11-p21)**2)+((p12-p22)**2))

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

    #sumofsquareerror = 0
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
        #if (oldCluster != kForMin):
            #sumofsquareerror += 1
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
        mycentroid = mycentroidcol.find_one({"_id":x["cluster"]})
        sumofsquareerror += dist_between_points(float(x["kmeansNorm"][0]),float(x["kmeansNorm"][1]),mycentroid["kmeansNorm"][0],mycentroid["kmeansNorm"][1])
    #print("movie")

        
    return sumofsquareerror
 
genresToTry = ["Action","Horror","Romance","Sci-Fi","Thriller"]
# genresToTry = ["Sci-Fi","Thriller"]
kMaxTimes = 100
kStart = 10
kEnd = 50
kStep = 5

for genreIter in genresToTry:
    #print(genreIter)
    currKVal = kStart
    myXArr = []
    myYArr = []
    while(currKVal <= kEnd):
        myq2(genreIter, currKVal)
        numIterations = 0
        sumError = 0
        while (numIterations <= kMaxTimes):
            errorNow = my_kmeans_iteration(genreIter, currKVal)
            if errorNow == 0:
                break
            sumError += errorNow
            numIterations += 1
        #print(currKVal)
        print("K = "+str(currKVal)+ " Error Value: "+str(sumError))
        myXArr.append(currKVal)
        myYArr.append(sumError)
        currKVal += kStep
    plt.plot(myXArr, myYArr,linestyle='--', marker='o', color='b')
    plt.xlabel('k')
    plt.ylabel('square error')
    plt.title("Sum of Square Errors vs k for Genre = "+genreIter)
    plt.show()    
    getUserEnter = input("Press Enter to continue...")

    