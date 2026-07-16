class Solution:
    def stringMatching(self, words):
        return [word for i, word in enumerate(words)
                if any(i != j and word in other for j, other in enumerate(words))]
