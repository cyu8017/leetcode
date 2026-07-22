// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

using System;
using System.Linq;

public class Solution {
    public int BestTeamScore(int[] scores, int[] ages) {
        int n = scores.Length;
        var players = Enumerable.Range(0, n)
            .Select(i => (age: ages[i], score: scores[i]))
            .OrderBy(p => p.age).ThenBy(p => p.score)
            .ToArray();
        var dp = new int[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            dp[i] = players[i].score;
            for (int j = 0; j < i; j++) {
                if (players[j].score <= players[i].score)
                    dp[i] = Math.Max(dp[i], dp[j] + players[i].score);
            }
            ans = Math.Max(ans, dp[i]);
        }
        return ans;
    }
}
