islevel = 12
minsupport = 5
dropsql = "drop table L"+str(islevel)

if(islevel == 1):
    sqlstring = "Create table L1 as Select actor actor1, count(*) times_acted_together From Popular_Movie_Actors  Group by actor having count(*) > 5"
    print(dropsql)
    print(sqlstring)
    quit()
    
sqlstring = "create table L"+str(islevel)+" as select "
for i in range(islevel):
    sqlstring += "p"+str(i+1)+".actor actor"+str(i+1)+","
    #print(i)
sqlstring += " count(*) times_acted_together from Popular_Movie_Actors p1"
for i in range(islevel):
    if(i >0):
        sqlstring += " join Popular_Movie_Actors p"+str(i+1)+" on (p"+str(i)+".title = p"+str(i+1)+".title "
        for j in range(i):            
            sqlstring += " and p"+str(j+1)+".actor != p"+str(i+1)+".actor"
        sqlstring += ")"

sqlstring += " where 1 = 1 "

for k in range(islevel):
    sqlstring += " and ( "
    for i in range(islevel):
        if(i != k):
            sqlstring += "p"+str(i+1)+".actor,"
    sqlstring = sqlstring[:-1]
    sqlstring += ") in (select "
    for i in range(islevel):
        if(i>0):
            sqlstring += "actor"+str(i)+","
    sqlstring = sqlstring[:-1]
    sqlstring += " from L"+str(islevel-1)+")"

sqlstring += " group by "
for i in range(islevel):
    sqlstring += "p"+str(i+1)+".actor,"
sqlstring = sqlstring[:-1]
sqlstring += " having count(*) > "+str(minsupport)
print(dropsql)
print(sqlstring)

