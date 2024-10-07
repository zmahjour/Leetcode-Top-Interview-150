class Solution1:
    def can_construct(self, ransom_note, magazine):
        letters = {}
        for c in magazine:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        for c in ransom_note:
            if c not in letters:
                return False
            if letters[c] == 0:
                return False
            letters[c] -= 1   
        return True


class Solution2:
    def can_construct(self, ransom_note, magazine):
        letters = {}
        for s in magazine:
            letters[s] = letters.get(s, 0) + 1
            
        for s in ransom_note:
            if letters.get(s, 0) > 0:
                letters[s] -= 1
            else:
                return False
        return True
    

class Solution3:
    def can_construct(self, ransom_note, magazine):
        for s in ransom_note:
            if s not in magazine:
                return False
            magazine = magazine.replace(s, "", 1)
        return True
    

class Solution4:
    def can_construct(self, ransom_note, magazine):
        for s in set(ransom_note):
            if magazine.count(s) < ransom_note.count(s):
                return False
        return True