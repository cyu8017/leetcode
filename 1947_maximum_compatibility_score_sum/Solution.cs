// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

using System;
using System.Collections.Generic;

public class Solution {
    int m;
    int[][] score;
    Dictionary<(int, int), int> memo;

    public int MaxCompatibilitySum(int[][] students, int[][] mentors) {
        m = students.Length;
        score = new int[m][];
        for (int i = 0; i < m; i++) {
            score[i] = new int[m];
            for (int j = 0; j < m; j++) {
                int s = 0;
                for (int t = 0; t < students[i].Length; t++)
                    if (students[i][t] == mentors[j][t]) s++;
                score[i][j] = s;
            }
        }
        memo = new Dictionary<(int, int), int>();
        return Dp(0, 0);
    }

    int Dp(int i, int mask) {
        if (i == m) return 0;
        if (memo.TryGetValue((i, mask), out int cached)) return cached;
        int best = 0;
        for (int j = 0; j < m; j++)
            if ((mask & (1 << j)) == 0)
                best = Math.Max(best, score[i][j] + Dp(i + 1, mask | (1 << j)));
        return memo[(i, mask)] = best;
    }
}