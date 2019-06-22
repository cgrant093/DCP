import sys


def costCalc(costMatrix):

    if not costMatrix:
        return 0

    # sets previous house values to 0 or numbers it can't be since its the start of the matrix
    prevMin = 0
    prevMinIndex = -1
    prevSecondMin = 0

    # loops through the number of houses
    for i in range(len(costMatrix)):
        # in each house set both first and second min to largest possible number
        # and index to 0
        currMin = sys.maxsize
        currSecondMin = sys.maxsize
        currMinIndex = 0

        # now we loop through paint colors
        for j in range(len(costMatrix[0])):
            # if the previous color is the current color we are looking at
                # then set add current min color to previous second min color
            if prevMinIndex == j:
                costMatrix[i][j] += prevSecondMin
                # otherwise add current value to the previous minimum color
            else:
                costMatrix[i][j] += prevMin

            # if the current min color is greater than the current element
                # then set current second min to current min
                # current min color to value that's less
                # and set current min color index to j
            if currMin > costMatrix[i][j]:
                currSecondMin = currMin
                currMin = costMatrix[i][j]
                currMinIndex = j
            # else if second min color is greater than current element
                # then set second min color to current element
            elif currSecondMin > costMatrix[i][j]:
                currSecondMin = costMatrix[i][j]

        # finally move all currents to previous status before moving on in main for loop
        prevMin = currMin
        prevSecondMin = currSecondMin
        prevMinIndex = currMinIndex

    # since all values added together, the min of the last row will be the min cost
    return min(costMatrix[len(costMatrix) - 1])



#input matrix
costMatrix = \
    [[1, 2, 4],
    [3, 1, 2],
    [4, 3, 2]]

print("Minimum cost to paint all the houses is", costCalc(costMatrix))