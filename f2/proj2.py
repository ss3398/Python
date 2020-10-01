# Creates a Log log scatter plot of Distance vs # visits
# The input file was created in Oracle/SQL
import csv
import matplotlib.pyplot as plt

filename = 'hundred_ntile.csv'
dists = []
sEncCnt = []
rowCount = 0
with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        rowCount += 1
        dists.append(float(row[1]))
        sEncCnt.append(float(row[2]))

"""
print(len(dists))
print(len(sEncCnt))
print(dists)
print(sEncCnt)
print(min(dists))
print(min(sEncCnt))
print(max(dists))
print(max(sEncCnt))
"""

plt.clf() # reset the plot
plt.scatter(x = dists, y = sEncCnt)

plt.title('Distance vs Total Number of Visits (Log Log)')
plt.xlabel('Distance')
plt.ylabel('Total Number of Visits')
plt.xscale('log')
plt.yscale('log')
plt.savefig(fname='total_visits_vs_distance_log_log.png')
plt.show()


        
