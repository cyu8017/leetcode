class Solution:
    def countConsistentStrings(self, allowed, words):
        a=set(allowed);return sum(set(w)<=a for w in words)
