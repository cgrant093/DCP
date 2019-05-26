import numpy as np


#array of numbers
a = [1, 2, 3, 4]

# array where answers will be held
answers = np.ones(len(a))

for i in range(len(a)):
    for j in range(len(a)):
        if (j!=i):
            answers[i] = answers[i]*a[j]

print("The new array is:\n", answers)