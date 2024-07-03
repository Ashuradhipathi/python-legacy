#Input File name
file_name = input("Enter File: ")
handle = open(file_name,'r')

#count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

#Most common word
big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

#Return count, word
print(f"Count : {big_count} \n Word : {big_word}")