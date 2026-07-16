class Solution:
    def closeStrings(self, word1, word2):
        from collections import Counter
        a,b=Counter(word1),Counter(word2)
        return a.keys()==b.keys() and sorted(a.values())==sorted(b.values())
