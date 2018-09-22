lastDay = 365

# reads a work in a line and returns a tuple
def readLine():
    till, cost = [int(word) for word in input().split(" ")]
    return (till, cost)

N = int(input())
# read all works and append the id
works = [(i + 1,) + readLine() for i in range(N)]

# sort the works by the money they give
works.sort(key = lambda work : work[2], reverse = True)

# this list shows whether a day is occupied for work
occupied = [False] * (lastDay + 1)

# this occupies a day for a given work
# if it could be done it returns true
# if it could NOT be done it returns false
def occupyForWork(work):
    for i in range(work[1], 0, -1):
        if not occupied[i]:
            occupied[i] = True
            return True
    
    return False

# which works can be done
worksTodo = []
moneyEarned = 0

# go through works and do the ones that are still possible
for work in works:
    # work can be done
    if occupyForWork(work):
        worksTodo.append(work)
        moneyEarned += work[2]

print(moneyEarned)
for work in worksTodo:
    print(work[0])