def count_words(sentence):
    """Count words in sentence"""
    words = sentence.split(" ")
    return len(words)

print(count_words("This is a sentence with words in it"))
print(count_words(("Hello, my name is Luke, whats your's?")))