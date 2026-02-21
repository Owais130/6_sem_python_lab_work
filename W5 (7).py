def reverse_words_in_sentence(s):
    words = s.split(' ')
    
    reversed_words = [word[::-1] for word in words]

    return ' '.join(reversed_words)

sentence = "Hello world"
result = reverse_words_in_sentence(sentence)
print(result)  # Output: "olleH dlrow"
