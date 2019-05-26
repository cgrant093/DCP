import numpy as np


#array of numbers
a = [10, 15, 3, 7, 2, 4, 6, 8, 9, 25, 6]

#sum that any two can add up to
k = 17

# 2 column array where answers will be held
answers = np.full((len(a),2), 0)

# minimum row location for second column pair
j=0;

for i in range(len(a)):
    if (i>j):
        # will run through all open second columns
        for m in range(j,i+1):
            # base case if no pairs found
            if (m==i):
                answers[m][0]=a[i]
            # tests open pair to see if matches
            elif (a[i]+answers[m][0]==k) :
                answers[m][1]=a[i]
                #increases minimum row location
                j += 1
    #base case when i==j
    else:
        answers[i][0]=a[i]

print("The possible pairs that equal ", k, " are:\n")

# prints only filled pairs
# this needs work if '0' can be an element of the array
for i in range(len(answers)):
    if (answers[i][1] != 0):
        print("(", answers[i][0], ", ", answers[i][1], ")\n")