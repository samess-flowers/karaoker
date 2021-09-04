#!/usr/bin/python3
from sys import argv

in_file = argv[1]
#in_minutes = argv[2]
#in_seconds = argv[3]

text_file = open(in_file, 'r')
text = text_file.read()
text_file.close()

#cleanup
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

#get word count
word_count = len(words)
print(word_count)

word_freq = []
for w in words:
    word_freq.append(words.count(w))

sort_freq = sorted(list(set(word_freq)))
print(sort_freq)
word_list = list(set(zip(words, word_freq)))
sort_list = (sorted(word_list, key = lambda x: x[1]))

#get unique words
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
unique_count = len(unique)
list_count = len(words)

#twenty_number = int(list_count * .2)
#print(twenty_number)
top_twenty = sort_list[0:(int(list_count * .4))]
last_twenty = sort_list[-(int(list_count * .1)):]
last_twenty_count = 0
print(last_twenty_count)
print(top_twenty)
print(last_twenty)

exit()
#get length
#length = float(input("How long is this song? "))
minutes = float(in_minutes)
seconds = (float(in_seconds) / 60)
length = minutes + seconds
#do math on counts
    #words/length
pace = word_count / length
    #unique/words
diversity = unique_count / word_count
    #unique/length
interest = unique_count / length
#display metrics

print(f"For file {in_file} with length of {in_minutes}:{in_seconds}:")
print(word_count , length , unique_count)
print("Song pace (w/l) is: " , pace)
print("Song diversity (u/w) is: " , diversity)
print("Song interest (u/l) is: " , interest, "\n")
