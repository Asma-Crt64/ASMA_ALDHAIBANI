def reverse_words(sentence):
    words = sentence.split()  
    reversed_sentence = ' '.join(reversed(words))  
    return reversed_sentence


print(reverse_words("Hello world Python"))
