# LeetCode 0544 - Output Contest Matches
# https://leetcode.com/problems/output-contest-matches/

class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = [str(i) for i in range(1, n + 1)]
        while len(teams) > 1:
            next_round = []
            for i in range(len(teams) // 2):
                next_round.append(f"({teams[i]},{teams[-1 - i]})")
            teams = next_round
        return teams[0]
