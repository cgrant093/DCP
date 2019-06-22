import random as rnd

# define stream of data
streamOfData = []

# i is latest element of data stream and updates as the stream comes in
i.updateToLastest()

while streamOfDataIsActive:
    #find random number of past 1000 element (or whatever number is reasonable)
    n = rnd.uniform[0, 1000]

    # save that random number
    streamOfData[i-n].save()

    # update i if more elements have come in
    i.updateToLatest()


