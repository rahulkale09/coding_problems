#Check whether the character is vowel or consonent

def char_check():
    c = str(input('Enter a character: '))

    if c in 'aeiou':
        print('The character is in the vowel.')
    else:
        print('The character is the consonant.')

char_check()