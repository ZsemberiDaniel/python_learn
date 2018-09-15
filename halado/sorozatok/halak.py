fishCount = int(input())

forbidden = [[int(line[0]), int(line[1])] for line in [input().split(" ") for i in range(fishCount)]]
forbidden.sort()

notForbidden = []

currForbidden = forbidden[0]
# print if at start of year it is not forbidden
if currForbidden[0] > 1:
    notForbidden.append((1, currForbidden[0] - 1))

# print inside year
for timeSpan in forbidden:
    # if the current forbidden timespan's start is in the forbidden timespan
    if currForbidden[0] <= timeSpan[0] <= currForbidden[1] + 1:
        # expand the end of the forbidden timespan if needed
        currForbidden[1] = max(currForbidden[1], timeSpan[1])
    else: # the current timespan's start is outside of forbidden timespan
        notForbidden.append((currForbidden[1] + 1, timeSpan[0] - 1))

        currForbidden = timeSpan

# print end of year
if currForbidden[1] < 365:
    notForbidden.append((currForbidden[1] + 1, 365))

print(len(notForbidden))
for timeSpan in notForbidden:
    print(timeSpan[0], timeSpan[1])