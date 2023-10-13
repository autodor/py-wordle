import io
import os
import random

#print('\033[2;31;43m CHEESY')

with open('py-wordle/words.txt', 'r') as f:
    ##get words in each line
    data = f.readlines()
    randomNumber = random.randrange(0,len(data))
    ##print (len(data))
    selected_word = (data[randomNumber]).rstrip('\n')
    selected_word = "guage"
    print (selected_word)
#selected_word = "first"
#guesses_remaining = 5
guess = ''

# create a dictionary to store letter counts for the selected word
selected_letter_count = {}
for l in selected_word:
    x = selected_letter_count.get(l)
    if x is None:
        selected_letter_count[l] = 1
    else:
        selected_letter_count.update({l : x+1})

#create a list of the letters in the word to help identify if there 
#are any letters in the right spot
selected_word_ltr_index = ([*selected_word])

print (selected_word_ltr_index[2])
    
    
print (selected_letter_count)
    
#does guess = word?
while (guess != selected_word):
    guess = input("Provide a guess: ")
    
    #verify guess is exactly 5 characters long
    if (len(guess) == 5):
        print (guess == selected_word)
        if (guess == selected_word):
            print ('you won!')
        else:
            #create a copy of the selected word dictionary
            tmpLetterDict = selected_letter_count.copy()
            
            ##IDEA - instead of looping through the guess, why not loop through the selected word?
            
            
            for g_idx, g in enumerate(guess):
                #does letter exist in the selected word dictionary?
                if selected_letter_count.get(g) is None:
                    #letter does not exist in selected word dictionary
                    print (g + " does not exist in the word")
                else:
                    if selected_word_ltr_index[g_idx] == g:
                        #does letter exist in same index?
                        print (g + " is in the right spot" )
                        
                        #subtract one instance of letter from tmpLetterDict
                        #guessed letter exists. remove letter from tmp dictionary
                        
                        #print ("there are " + str(dictCount) + " " + g + "'s in the word. removing one from the tmp dictionary")
                        tmpLetterDict.update({g : tmpLetterDict.get(g) - 1})
                    
                    
                    else:
                        #letter exists but not in this index
                        
                        
                        #TODO: if correct index is greater than current index and remaining letter count = 1 then does not exist
                        
                        #if 
                        
                        
                        if tmpLetterDict.get(g) >= 0:
                            #does 
                            print(g + " is in the wrong spot")
                        else:
                            print (g + " does not exist in the word")
                        
                    
            
    else:
        print ("word must be 5 letters")
