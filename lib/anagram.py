# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        
        matches = []

        for candidate in word_list:
            if self.is_anagram(candidate):
                matches.append(candidate)

    
        return matches

    def is_anagram(self, candidate):
    
        return sorted(self.word.lower()) == sorted(candidate.lower())
