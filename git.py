def count_words(sentence):
    count = {} #12345
    sentence = sentence.lower()
    sentence = sentence.split()
    for word in sentence:
        count[word] = count.get(word,0) + 1
    count = sorted(count.items(), key=lambda pair: pair[1])
    return count

for word, number in count_words("the cat saw the Cat"):
    print (f"{word}: {number}")