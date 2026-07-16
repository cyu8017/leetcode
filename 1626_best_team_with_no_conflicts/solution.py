class Solution:
    def bestTeamScore(self, scores, ages):
        players = sorted(zip(ages, scores)); dp = [0] * len(players)
        for i, (_, score) in enumerate(players):
            dp[i] = score + max((dp[j] for j in range(i) if players[j][1] <= score), default=0)
        return max(dp, default=0)
