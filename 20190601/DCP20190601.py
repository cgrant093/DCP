# find substring function
def findSubstr(s, k, i):
    if k > len(s):
        return 0

    elif k == len(s):
        return k

    else:

        if s[i+1] == s[i]:
            return 1 + findSubstr(s, k, i+1)

        else:
            letterExists = False
            for j in range(i):
                if s[j] == s[i+1]:
                    letterExists == True
                    break

            if letterExists:
                return 1 + findSubstr(s, k, i+1)

            else:
                notEqWFirst = 1 + findSubstr(s, k-1, i+1)
                notEqWOFirst = findSubstr(s, k, i+1)

                return max(notEqWFirst, notEqWOFirst)

s = "abcbca"
k = 2
print(findSubstr(s, k, 0))

#for i in range(len(s)):
#    if len(s[i:]) < k:
 #       print("String doesn't have", k, "unique characters")
  #      break

   # elif i == len(s)-1 and k == 1
    #    else:
     #       ssLength += 1





