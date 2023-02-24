# your code goes here!

class Anagram:
    def __init__(self,word):
        self.word = word
    
    def match(self,lists):
        i = 0
        matched = []
        if len(lists) == 0:
            return matched
        # new = [x for x in word]
        while i < len(lists):
            # match = [x for x in lists[i]]
            if sorted([x for x in self.word]) == sorted([x for x in lists[i]]):
                matched.append(lists[i])
            i+=1
        return matched