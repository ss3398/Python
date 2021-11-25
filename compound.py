import re #regular expressions standard package of python
import urllib3 #standard python library to handle URLs
import sys

def loadAtomicWeights():
    url = "http://nob.cs.ucdavis.edu/classes/mhi289i-2021-04/homework/atomic_weights.txt"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    myres = response.data.decode("utf-8")
    myDict = {}

    for myline in myres.splitlines():
        linecontent = myline.split()
        #print("Symbol is "+linecontent[1] + " at mass is "+linecontent[0])
        myDict[linecontent[1]] = linecontent[0]
        
    return myDict

def extractElementsAndNums(molecule):
    myElementsArr = re.findall('[A-Z][a-z]?|\d+|.', molecule)
    lasttoken = ""
    myDict = {}
    currCount = 0
    for mytoken in myElementsArr:
        #print(mytoken)
        if(lasttoken == ""):
            lasttoken = mytoken
            continue
        if(mytoken.isdigit()):
            currCount = myDict.get(lasttoken,0)
            myDict[lasttoken] = currCount + int(mytoken)
        else:
            if(lasttoken.isdigit() == False):
                currCount = myDict.get(lasttoken,0)
                myDict[lasttoken] = currCount + 1
        # if curr token is a number
        #     enter the prev token and curr token as pair to dict
        # else
        #     if prev token is a number
        #         do nothing
        #     if prev token is an element
        #         enter prev token and 1 as pair to dict
        # outside the for loop if prev token is an element, enter prev token and 1 as pair to dict
        lasttoken = mytoken
    if(lasttoken.isdigit() == False):
        currCount = myDict.get(lasttoken,0)
        myDict[lasttoken] = currCount + 1
    return myDict

while True:
    print("Chemical Composition? ",end='')
    molformula = sys.stdin.readline()
    if(molformula):
        pass
    else:
        break
    if(molformula == "" or molformula == "\n"):
        break
    myelements = extractElementsAndNums(molformula)
    myAtWeightsDict = loadAtomicWeights()
    totalAtWt = 0.0
    for myElement in myelements.keys():
        totalAtWt += float(myelements[myElement])*float(myAtWeightsDict[myElement])
    #print(myelements)
    print("The atomic weight of "+ molformula + " is " + str(totalAtWt))


    