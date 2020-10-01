# For creating a linear regression model

import matplotlib.pyplot as plt
import csv
import math
from scipy import stats

filename = 'hundred_ntile.csv'
dists = []
sEncCnt = []
rowCount = 0
ldists = []
lsEncCnt = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        rowCount += 1
        dists.append(float(row[1]))
        sEncCnt.append(float(row[2]))

for i in dists:
    ldists.append(math.log(i))
for i in sEncCnt:
    lsEncCnt.append(math.log(i))

slope, intercept, r, p, std_err = stats.linregress(ldists, lsEncCnt)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, ldists))

plt.clf() # reset the plot
plt.scatter(x = ldists, y = lsEncCnt)

plt.title('Distance vs Total Number of Visits (Log Log plot)')
plt.xlabel('Distance')
plt.ylabel('Total Number of Visits')
plt.plot(ldists, mymodel)
plt.savefig(fname='model_total_visits_vs_distance.png')
plt.show()

