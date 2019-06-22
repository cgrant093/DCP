def splitSentence(s, words):

    if not s or not words:
        return []

    # make a word set out of our library
    word_set = set(words)
    # make a blank sentence list of words
    sentence_words = list()

    for i in range(len(s)):
        # if word is in the word set
            # then add thework to the sentence list
            # and remove from word set
            # then recursively call with smaller sentence and library
        if s[0:i+1] in word_set:
            sentence_words.append(s[0:i+1])
            word_set.remove(s[0:i+1])
            sentence_words += splitSentence(s[i+1:], word_set)

            break

    return sentence_words






sentence1 = "thequickbrownfox"
library1 = ['quick', 'brown', 'the', 'fox']
sentence2 = "bedbathandbeyond"
library2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']

print("The sentence", sentence1, "decomposes to", splitSentence(sentence1, library1))
print("The sentence", sentence2, "decomposes to", splitSentence(sentence2, library2))