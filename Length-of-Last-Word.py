class Solution1:
    def length_of_last_word(self, s):
        word_len = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            word_len += 1
            i -= 1

        return word_len


# Best Solution
class Solution2:
    def length_of_last_word(self, s):
        word_len = 0
        i = len(s) - 1

        while i >= 0:

            if s[i] != ' ':
                word_len += 1
            elif word_len != 0:
                break
            i -= 1

        return word_len
    

class Solution3:
    def length_of_last_word(self, s):
        words = s.strip().split()

        return len(words[-1])