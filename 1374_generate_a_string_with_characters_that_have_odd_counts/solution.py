class Solution:
    def generateTheString(self, n):
        return 'a'*n if n%2 else 'a'*(n-1)+'b'
