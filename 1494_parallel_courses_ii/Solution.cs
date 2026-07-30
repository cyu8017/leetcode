// LeetCode 1494 - Parallel Courses Ii
// https://leetcode.com/problems/parallel-courses-ii/

using System.Collections.Generic;
using System.Numerics;
public class Solution {
    public int MinNumberOfSemesters(int n, int[][] relations, int k) {
        var prereq = new int[n];
        foreach (var e in relations) prereq[e[1] - 1] |= 1 << (e[0] - 1);
        int full = (1 << n) - 1, inf = 1000000000;
        var dp = new int[1 << n];
        for (int i = 0; i < dp.Length; i++) dp[i] = inf;
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == inf) continue;
            int available = 0;
            for (int c = 0; c < n; c++)
                if (((mask >> c) & 1) == 0 && (prereq[c] & mask) == prereq[c])
                    available |= 1 << c;
            var choices = new List<int>();
            if (BitOperations.PopCount((uint)available) <= k) choices.Add(available);
            else {
                for (int sub = available; sub > 0; sub = (sub - 1) & available)
                    if (BitOperations.PopCount((uint)sub) == k) choices.Add(sub);
            }
            foreach (int take in choices)
                dp[mask | take] = System.Math.Min(dp[mask | take], dp[mask] + 1);
        }
        return dp[full];
    }
}
