def minNumOfRooms(lectureTimes):
    if not lectureTimes:
        return 0

    # create a diction for start and end times
    startTimes = dict()
    endTimes = dict()

    # double for loop that adds start times to startTimes dictionary
    # and end times to endTimes dictionary
    for start, end in lectureTimes:
        if start not in startTimes:
            startTimes[start] = 0
        startTimes[start] += 1

        if end not in endTimes:
            endTimes[end] = 0
        endTimes[end] += 1

    # make global start and end times
    globalStart, globalEnd = min(startTimes), max(endTimes)

    maxClassCount = 0
    currClassCount = 0

    for i in range(globalStart, globalEnd):
        # if i in start times
            # then add current class count to start time
        if i in startTimes:
            currClassCount += startTimes[i]
            # and if current class count is greater tha max class count
                # then max is set equal to current
            if currClassCount > maxClassCount:
                maxClassCount = currClassCount

        # if i in end times
            # then add end times to current class count time
        if i in endTimes:
            currClassCount -= endTimes[i]

    return maxClassCount




lectureTimes = [[30, 75], [0, 50], [60, 150]]

print("Number of rooms you'll need is", minNumOfRooms(lectureTimes))
