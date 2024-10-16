# Best Solution
class Solution1:
    def roman_to_int(self, s):
        mapping = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        answer = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and mapping[s[i]] < mapping[s[i + 1]]:
                answer -= mapping[s[i]]
            else:
                answer += mapping[s[i]]
        return answer
    

class Solution2:
    def roman_to_int(self, s):
        mapping = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        answer = 0
        i = 0
        while i < len(s):
            if s[i:i + 2] in mapping:
                answer += mapping[s[i:i + 2]]
                i += 2
            else:
                answer += mapping[s[i]]
                i += 1
        return answer


class Solution3:
    def roman_to_int(self, s):
        mapping = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        to_change = {'IV': 'IIII', 'IX': 'VIIII', 'XL': 'XXXX', 'XC': 'LXXXX', 'CD': 'CCCC', 'CM': 'DCCCC'}
        for num in to_change:
            s = s.replace(num, to_change[num])
        answer = 0
        for char in s:
            answer += mapping[char]
        return answer