#!/usr/bin/python3
from sys import argv

in_file = argv[1]
in_minutes = argv[2]
in_seconds = argv[3]

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

#get unique words
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
unique_count = len(unique)

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
