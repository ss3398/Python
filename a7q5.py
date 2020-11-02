islevel = 4
minsupport = 5
dropsql = "drop table L"+str(islevel)
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

sqlstring += " where ("
for i in range(islevel):
    if(i>0):
        sqlstring += "p"+str(i)+".actor,"
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
