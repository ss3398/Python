import random

# This function returns 1 or 2 or 3 randomly.
def get_rand():
    hl = 3 # the upper limit. The lower limit is 1.
    # get the random fraction between 0 and 1, multiply it with the upper limit and then add 1 so the lower limit becomes 1.
    return 1+int(hl*(random.random()))

# Helper function. Takes two numbers and returns the third number (out of 1, 2 and 3).
# This function is called to decide which "door" to open. Also to switch the choice of door.
def getThirdNum(firstNum, secondNum):
    # in case the two numbers passed are the same, send either of the other two. 
    if (firstNum == secondNum):
        # if 3 was passed, return 1
        if(firstNum == 3):
            return 1
        else:
            # if 1 or 2 was passed, add 1 and return it
            return firstNum + 1
    else:
        # The two numbers are different. 
        if(firstNum == 1):
            if(secondNum == 2):
                # if 1 and 2 were passed, return 3
                return 3
            else:
                # if 1 and 3 were passed, return 2
                return 2
        elif (firstNum == 2):
            if(secondNum == 1):
                # if 1 and 2 were passed, return 3
                return 3
            else:
                # if 3 and 2 were passed, return 1
                return 1        
        else:
            if(secondNum == 1):
                # if 3 and 1 were passed, return 2
                return 2
            else:
                # if 3 and 2 were passed, return 1
                return 1
    

# In this function, we always switch our choice.
def montyalways():
    # This is the door where the prize is actually there
    realPrize = get_rand()
    # The initial guess of the right door
    initialGuess = get_rand()
    # This door is "opened". The parameters sent include the actual door with prize. So toOpen NEVER has the prize.
    toOpen = getThirdNum(realPrize,initialGuess)
    # We switch the guess 
    newGuess = getThirdNum(initialGuess,toOpen)
    # check if the new guess is correct and return True or False based on that.
    return newGuess == realPrize

# In this function, we do not switch our choice.
def montynever():
    # This is the door where the prize is actually there
    realPrize = get_rand()
    # The initial guess of the right door
    initialGuess = get_rand()
    # This door is "opened". The parameters sent include the actual door with prize. So toOpen NEVER has the prize.
    toOpen = getThirdNum(realPrize,initialGuess)
    # We do not switch here. Keep the same guess.
    newGuess = initialGuess
    # check if the new guess is correct and return True or False based on that.
    return newGuess == realPrize


# Ask the user to input the number of games
userInput = input("Number of games to play: ")
cleanedInput = 0
try:
    # try to convert the user input into an integer
    cleanedInput = int(userInput)
except:
    # oops. The user entered something that is not an integer
    print("Please enter a positive integer")
    quit()

# Also, check if the number entered is at least 1. If not, quit.
if(cleanedInput < 1):
    print("Please enter a positive integer")
    quit()

# Show what was entered by the user.
print("\n\nOut of "+str(cleanedInput)+ " games:")

# Initialize success count to zero.
successCount = 0
for x in range(cleanedInput):
    # Check if we won the monty hall problem if we switch
    if(montyalways()):
        # if We won, increment the success count by 1
        successCount += 1
# Print how many times and what fraction we won        
print("Always switching wins: "+str((1.0*successCount)/cleanedInput) + " ("+str(successCount) + " games)")

# Initialize success count to zero.
successCount = 0
for x in range(cleanedInput):
    # Check if we won the monty hall problem if we do not switch
    if(montynever()):
        # if We won, increment the success count by 1
        successCount += 1  
# Print how many times and what fraction we won        
print("Never switching wins: "+str((1.0*successCount)/cleanedInput) + " ("+str(successCount) + " games)")





