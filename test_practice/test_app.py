import string 
import numpy as np 
import random
from words import data


def load_file(data: list ):
    name_countries=[]
    
    for x in data:
      name_countries.append(x.strip("\n"))
    data.close()
    return name_countries


def mask_word(word):
    masked_word=''
    for character in word:
        if(character!= None):
            masked_word=masked_word+'*'
        else:
            masked_word=masked_word+' '
    return masked_word  


def select_letter(letters):
    index=-1
    while(index==-1):
        l=input("Choose Letter: ")
        try:
            index=letters.index(l)
        except:
            print("Letter not in the list! Try again!")
    return [index,l]

