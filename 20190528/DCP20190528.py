# define find max sum function
def maxSum(numList):

    if not numList:
        return 0

    # if list is 1 or 2 elements, return the max
    elif len(numList) <= 2:
        return max(numList)

    else:
        # take off first element
        firstElem = numList[0]

        # take max all elements (except the first two) and add the first
        sumWithFirst = firstElem + maxSum(numList[2:])

        # and take all elements except the first and find max
        sumWithoutFirst = maxSum(numList[1:])

        # compare two numbers to see which is greater
        return max(sumWithFirst, sumWithoutFirst)





# define array list
#a = [2, 4, 6, 2, 5]
#a = [5, 1, 1, 5]
a = [2, -14, 6, 0, 5, 8]


print("The max sum of ", a, " is ", maxSum(a))