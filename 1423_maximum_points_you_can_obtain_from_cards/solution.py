class Solution:
    def maxScore(self, cardPoints, k):
        if k == len(cardPoints):
            return sum(cardPoints)
        window = len(cardPoints) - k
        current = sum(cardPoints[:window])
        smallest = current
        for i in range(window, len(cardPoints)):
            current += cardPoints[i] - cardPoints[i - window]
            smallest = min(smallest, current)
        return sum(cardPoints) - smallest
