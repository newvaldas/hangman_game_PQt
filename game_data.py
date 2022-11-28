import random

class GameData():
    
    def __init__(self) -> list: 

        """
        initialize GameData by reading dictionary file and add each 
        word to a list
        """
        with open("dictionary.txt") as word_file:
            self.words = word_file.read().splitlines()
            
            
    def get_word(self) -> str:
        """
        returns a random word with 3 or more characters 
        """
        word = ""
        while len(word) < 3:
            word = random.choice(self.words)
            return word