# first lets alphabetize the dictionary
a = ["dog", "deer", "deal"]
sortA = sorted(a)

# define query string
qs = "de"


print("The following works were found to match '", qs, "':\n")

for i in range(len(sortA)):

    # since alphabetized, if it's after the query string, just break the for loop
    if sortA[i][:len(qs)] > qs:
        break

    # if it equals the query string, print whole entry
    elif sortA[i][:len(qs)] == qs:
        print(sortA[i])

