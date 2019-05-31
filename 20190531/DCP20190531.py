# define step counting function

def stepCount(N, X):
    # 2 base cases
    if N == 0:
        return 1

    elif N < min(X):
        return 0

    else:
        # define step counter
        numSteps = 0

        # count steps for smaller staircases and add together
        for i in range(len(X)):
            numSteps += stepCount(N-X[i], X)

        return numSteps


N = 4
X = [1, 2]

print("The number of ways to climb", N, "steps with")
print(X, "steps at a time is", stepCount(N, X))
