# Exercise 2: Randomness Test
import random

def lotteryGame(ballsList) -> list:
    randomBalls = []
    for _ in range(10):
        randBall = random.choice(ballsList)
        randomBalls.append(randBall)
        ballsList.remove(randBall)
    randomBalls.sort()
    return randomBalls
        
returnList = lotteryGame(list(range(50)))

# Unit test
assert type(returnList) == list
returnList_sorted = returnList.copy()
returnList.sort()
print(returnList_sorted == returnList)


# total time used: 19 mins
# Unit test method - check if the return value has type of list or not using assert command
#                    and also check if the returned value is already sorted ascendingly or not using the return value itself 
#                    compare with ascending sort of its value again.