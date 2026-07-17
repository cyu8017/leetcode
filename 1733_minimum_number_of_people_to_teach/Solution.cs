// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumTeachings(int n, int[][] languages, int[][] friendships) {
        int users = languages.Length;
        bool[,] knows = new bool[users, n + 1];
        for (int user = 0; user < users; user++) {
            foreach (int lang in languages[user]) {
                knows[user, lang] = true;
            }
        }
        var need = new HashSet<int>();
        foreach (int[] friendship in friendships) {
            int u = friendship[0] - 1;
            int v = friendship[1] - 1;
            bool shares = false;
            foreach (int lang in languages[u]) {
                if (knows[v, lang]) {
                    shares = true;
                    break;
                }
            }
            if (!shares) {
                need.Add(u);
                need.Add(v);
            }
        }
        if (need.Count == 0) {
            return 0;
        }
        int best = int.MaxValue;
        for (int lang = 1; lang <= n; lang++) {
            int teach = 0;
            foreach (int user in need) {
                if (!knows[user, lang]) teach++;
            }
            best = Math.Min(best, teach);
        }
        return best;
    }
}
