text = input("Enter your sentence: ")
text = text.upper()
words = text.split()

word_count = {}
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

# Display the result
print(word_count)
