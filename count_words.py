#open text file in read mode
text_file = open("./total.txt", "r")
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

counted = word_count(data.lower())

for w in sorted(counted, key=counted.get, reverse=False):
    print(w, counted[w])
