import pymongo
import pandas as pd
import matplotlib.pyplot as plt 
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

#client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
client = pymongo.MongoClient("localhost",27017)

result = client['mikedb']['movie2'].aggregate([
    {
        '$group': {
            '_id': '$startYear', 
            'numMovies': {
                '$sum': 1
            }
        }
    }
])
dfresult = pd.DataFrame(list(result))
dfresult2 = dfresult.sort_values(by=['_id'])
dfresult2.rename(columns={'_id':'startYear'},inplace=True)
dfresult2.plot(x='startYear',y='numMovies',kind='line')
plt.show()



