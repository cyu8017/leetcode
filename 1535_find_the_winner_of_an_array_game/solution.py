# LeetCode 1535

class Solution:
    def getWinner(self, arr, k):
        champion, wins = arr[0], 0
        for challenger in arr[1:]:
            if champion > challenger:
                wins += 1
            else:
                champion, wins = challenger, 1
            if wins == k:
                break
        return champion
