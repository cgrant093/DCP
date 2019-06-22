# doing it with arrays because same concept

A = [3, 7, 8, 10]
B = [99, 1, 8, 10]

mergedAndSorted = sorted(A+B)

hadDouble = False

print(mergedAndSorted)

for i in range(len(mergedAndSorted)):
    if mergedAndSorted[i] == mergedAndSorted[i+1]:
        hadDouble = True
        print("The intersection point is", mergedAndSorted[i])

    if hadDouble == True:
        break

if hadDouble == False:
    print("No intersection points")