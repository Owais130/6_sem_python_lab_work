text = input("Enter a text: ")
text = text.lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0
vowel_list = []
consonant_list = []

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)
        else:
            consonant_count += 1
            consonant_list.append(char)


print("Vowels:", vowel_list)
print("Number of vowels:", vowel_count)
print("Consonants:", consonant_list)
print("Number of consonants:", consonant_count)
