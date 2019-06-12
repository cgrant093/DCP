# initialize array a and subarray length k
a = [10, 5, 2, 7, 8, 7]
k = 3

print("The max values of each subarray in", a, "for k =", k, " is: ")

#for loop that iterates through k-1 to the length of array a
for i in range((k-1), len(a)):
    # prints the max value of the subarray
    print(max(a[i-k+1:i+1]))
