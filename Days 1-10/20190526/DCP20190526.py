# encoded string

codeMessage = '010'
codeLetters = list(codeMessage)


def countUpNum(code, i):
    # if last element, only one option
    if i == (len(code)-1):
        return 1

    else:
        j = countUpNum(code, i+1)

        # two special cases, 2 (with a follow up of 0 to 6) and 1
        if (int(code[i])==2 and int(code[i+1]) < 7) or (int(code[i])==1):
            # if second to last element, just add 1 to answer
            if i == (len(code)-2):
                return j+1
            # otherwise, count up all possibilites of next element and 2 elements from now
            else:
                return (j + countUpNum(code, i+2))

        # if not a special case, then just count up all possibilities of next element
        else:
            return j

numOfCodes = countUpNum(codeLetters, 0)

print("Number of possible codes for ", codeMessage, " is ", numOfCodes)