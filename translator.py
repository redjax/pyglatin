pyg = 'ay'

original = raw_input('Enter a word to be translated into Pig Latin: ') #sets original to a user-input word

if len(original) > 0 and original.isalpha(): #if statement determines if the length of inputted word is greater than 0
                                             # characters, and ensures it is a letter of the alphabet and not a number.

    word = original.lower() #sets variable 'word' to the lowercase of user inputted var

    first = word[0] #sets var 'first' to the first character of var 'word'

    if first == ('a' or 'e' or 'i' or 'o' or 'u'): #checks if first character is a vowel
        new_word = word + pyg #sets var 'new_word' to input plus var 'pyg'
        print 'Your translated word is ' + new_word
    else:
        new_word = (word[1: ] + (word[0] + pyg)) #moves first letter to end of the word and adds var 'pyg', then concats
        # var 'new_word' without first letter

        print 'Your translated word is ' + new_word #prints consonant version of var 'new_word' translated to Pig Latin
else:
    print 'empty' #if none of the before criteria are met, the word "empty" will be printed instead

#print 'Your translated word is ' + new_word #prints vowel version of var 'new_word' translated to Pig Latin
