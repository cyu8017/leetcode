class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars, opens = list(s), []
        for i, ch in enumerate(chars):
            if ch == '(': opens.append(i)
            elif ch == ')':
                if opens: opens.pop()
                else: chars[i] = ''
        for i in opens: chars[i] = ''
        return ''.join(chars)
