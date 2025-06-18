def shift_letters(word):
    result = ""
    for letter in word:
        if letter == 'z':
            result += 'a'
        elif letter == 'Z':
            result += 'A'
        elif letter.isalpha():
            result += chr(ord(letter) + 1)
        else:
            result += letter
    return result

print(shift_letters("hello"))  
print(shift_letters("Zebra"))  
print(shift_letters("xyz123!"))  
