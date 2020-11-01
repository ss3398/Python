# Requires the PyMongo package.
# https://api.mongodb.com/python/current
import json
import pymongo

client = pymongo.MongoClient("localhost",27017)
db = client["mikedb"]
mymoviecol = db["movie2"]
myextradatacol = db["extradata2"]
mymoviecombinedcol = db["moviecombined2"]

mymoviedoc = mymoviecol.find()
moviedocCount = 0
matchCount = 0

for x in mymoviedoc:
    moviedocCount += 1
    myquery = '{"IMDb_ID" : {"type":"literal","value":"' + x["_id"]+'"}}'
    #print(myquery)
    combinedJson = '{'
    try:
        combinedJson = combinedJson + '"_id":"' + str(x["_id"])+'",'
    except:
        print("No id")
    try:
        combinedJson = combinedJson + '"runtime":"' + str(x["runtime"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"startYear":"' + str(x["startYear"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"title":"' + str(x["title"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"originalTitle":"' + str(x["originalTitle"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"avgRating":"' + str(x["avgRating"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"type":"' + str(x["type"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"numVotes":"' + str(x["numVotes"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"genres":"' + str(x["genres"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"producers":"' + str(x["producers"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"actors":"' + str(x["actors"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"directors":"' + str(x["directors"])+'",'
    except:
        None
    try:
        combinedJson = combinedJson + '"writers":"' + str(x["writers"])+'",'
    except:
        None
    for y in myextradatacol.find(json.loads(myquery)):
        matchCount += 1
        try:
            combinedJson = combinedJson + '"box_office_currencyLabel":' + str(json.dumps(y["box_office_currencyLabel"]))+','
        except:
            None
        try:
            combinedJson = combinedJson + '"cost":' + str(json.dumps(y["cost"]))+','
            #print("Cost is " + str(json.dumps(y["cost"])))
        except:
            None
        try:
            combinedJson = combinedJson + '"distributorLabel":' + str(json.dumps(y["distributorLabel"]))+','
        except:
            None
        try:
            combinedJson = combinedJson + '"box_office":' + str(json.dumps(y["box_office"]))+','
        except:
            None
        try:
            combinedJson = combinedJson + '"MPAA_film_ratingLabel":' + str(json.dumps(y["MPAA_film_ratingLabel"]))+','
        except:
            None
        break
    combinedJson = combinedJson[:-1] + '}'
    mymoviecombinedcol.insert_one(json.loads(combinedJson))
    #print(combinedJson)
print("Number of Movies is " + str(moviedocCount) + ", Number of matches is "+str(matchCount)+".")

