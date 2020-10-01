# Reads the data, calculates the distance traveled based on zip codes
# The input file is created in Oracle using SQL
import pgeocode
import csv

filename = 'BHPatSiteDataAgg.csv'
rowNumber = []
patzips = []
sitezips = []
sEncCnt = []
dists = []

dist = pgeocode.GeoDistance('US')
#print(dist.query_postal_code('01510', '02155'))
rowCount = 0;
with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:        
        rowNumber.append(rowCount)
        patzips.append(row[0])
        sitezips.append(row[1])
        sEncCnt.append(row[2])
        dists.append(dist.query_postal_code(row[0], row[1]))
        #dists.append(1)
        #if(rowCount%100 == 0):
        #   print(str(rowCount)+" "+row[0] + " " + row[1] + " " + str(dist.query_postal_code(row[0], row[1])))
        rowCount += 1


with open('BHPatSiteDataAggWithDist.csv', mode='w') as pataggdist_file:
    pataggdist_writer = csv.writer(pataggdist_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    pataggdist_writer.writerow(['RowNumber','PAT_ZIP', 'SITE_ZIP', 'total_enc_cnt','distance_traveled'])
    for itrtr in range(rowCount):
        pataggdist_writer.writerow([rowNumber[itrtr],patzips[itrtr], sitezips[itrtr], sEncCnt[itrtr],dists[itrtr]])
    
