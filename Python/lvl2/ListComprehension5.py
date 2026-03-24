# You have a list of words. Use a Python list comprehension to create a new list where each word
# is converted to its length (a simple proxy for a vector dimension).

words = ["apple", "banana", "cherry", "mango", "grape", "jackfruit"]

word_lengths = [len(word) for word in words]
print(word_lengths)

#  Why it matters: Pythonic efficiency is key when handling massive amounts of textual data for NLP