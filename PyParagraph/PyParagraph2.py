import re

words = []
sentences = []
sentence_lengths = []
word_length_sum = 0
sentence_length_sum = 0

f = open("resources/paragraph_2.txt")
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

print("Paragraph Analysis")
print("-------------------")
print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(sentence_count))
print("Average Letter Count: " + str(avg_word_length))
print("Average Sentence Length: " + str(avg_sentence_length))

f = open('output/paragraph2_stats.txt','w')
f.write("Paragraph Analysis\n")
f.write("-------------------\n")
f.write("Approximate Word Count: " + str(word_count) + "\n")
f.write("Approximate Sentence Count: " + str(sentence_count) + "\n")
f.write("Average Letter Count: " + str(avg_word_length) + "\n")
f.write("Average Sentence Length: " + str(avg_sentence_length) + "\n")
f.close()