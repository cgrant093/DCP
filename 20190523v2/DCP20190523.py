
#input array
unsortedA = [2,0,1]

print(unsortedA)

#sort array
sortedA = sorted(unsortedA)

print(sortedA)

k=0; j=0;

for i in range(len(sortedA)):

# value has to be greater than or equal to zero
    if sortedA[i]>=0:
        # if first element, just set k = element + 1
        if i==0:
            k=sortedA[i]+1

        # if element is zero, just set k = 1
        elif sortedA[i]==0:
            k=1

        # if previous element is greater than or equal to zero then we check
        elif sortedA[i-1]>=0:
            # if current element is equal to k, then we add one to k
            if sortedA[i]==k:
                k+=1
            #else we break
            else:
                break

        # if previous element is less than 0, then we test
        elif sortedA[i-1]<0:
            #if current element equals 1, then set k=2
            if sortedA[i]==1:
                k=2
            # if it doesn't equal 1, then k=1 and break
            else:
                k=1
                break

    # if all elements are neg or 0, k=1 and break
    elif i == len(sortedA)-1:
        k=1
        break


print("The first missing positive integer is ", k)
