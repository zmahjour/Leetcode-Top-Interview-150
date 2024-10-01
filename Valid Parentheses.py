class Solution1(object):
    def is_valid(self, s):
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            elif not stack:
                return False
            elif char == ')':
                if stack.pop() != '(':
                    return False
            elif char == ']':
                if stack.pop() != '[':
                    return False
            elif char == '}':
                if stack.pop() != '{':
                    return False
            else:
                return False
        return not stack
    

class Solution2(object):
    def is_valid(self, s):
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in bracket_map:
                last_stack = stack.pop() if stack else None
                if bracket_map[char] != last_stack:
                    return False
            else:
                stack.append(char)
        return not stack