// LeetCode 1366 - Rank Teams By Votes
// https://leetcode.com/problems/rank-teams-by-votes/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public string RankTeams(string[] votes) {
        int m = votes[0].Length;
        var count = new Dictionary<char, int[]>();
        foreach (char c in votes[0]) count[c] = new int[m];
        foreach (var v in votes)
            for (int i = 0; i < v.Length; i++) count[v[i]][i]++;
        var teams = count.Keys.ToList();
        teams.Sort((a, b) => {
            for (int i = 0; i < m; i++) {
                int cmp = count[b][i].CompareTo(count[a][i]);
                if (cmp != 0) return cmp;
            }
            return a.CompareTo(b);
        });
        return string.Concat(teams);
    }
}
