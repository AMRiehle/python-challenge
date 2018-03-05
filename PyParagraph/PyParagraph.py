import re

words = []
sentences = []
sentence_lengths = []
word_length_sum = 0
sentence_length_sum = 0

f = open("resources/paragraph_1.txt")
paragraph = f.read()
paragraph = paragraph.replace("\n", " ")
paragraph = paragraph.replace("  ", " ")
paragraph = paragraph.replace('."', '".')
words = paragraph.split(" ")
sentences = re.split("(?<=[.!?]) +", paragraph)

for word in words:
    word_length_sum = word_length_sum + len(word)
    
for sentence in sentences:
    sentence_words = sentence.split(" ")
    sentence_lengths.append(len(sentence_words))

for length in sentence_lengths:
    sentence_length_sum = sentence_length_sum + int(length)

word_count = len(words)
avg_word_length = word_length_sum / word_count
sentence_count = len(sentences)
avg_sentence_length = sentence_length_sum / sentence_count

print(word_count)
print(avg_word_length)
print(sentence_count)
print(avg_sentence_length)