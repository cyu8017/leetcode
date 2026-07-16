class Solution:
    def checkPalindromeFormation(self, a, b):
        def check(x, y):
            i, j = 0, len(x) - 1
            while i < j and x[i] == y[j]: i += 1; j -= 1
            return x[i:j+1] == x[i:j+1][::-1] or y[i:j+1] == y[i:j+1][::-1]
        return check(a, b) or check(b, a)
