// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

using System.Collections.Generic;

public class Solution {
    public int MinArraySum(int[] nums, int k, int op1, int op2) {
        const long inf = (long)1e18;
        long[][] dp = new long[op1 + 1][];
        for (int a = 0; a <= op1; a++) {
            dp[a] = new long[op2 + 1];
            for (int b = 0; b <= op2; b++) dp[a][b] = inf;
        }
        dp[0][0] = 0;
        foreach (int x in nums) {
            long[][] ndp = new long[op1 + 1][];
            for (int a = 0; a <= op1; a++) {
                ndp[a] = new long[op2 + 1];
                for (int b = 0; b <= op2; b++) ndp[a][b] = inf;
            }
            for (int a = 0; a <= op1; a++) {
                for (int b = 0; b <= op2; b++) {
                    if (dp[a][b] == inf) continue;
                    var cand = new List<(int na, int nb, int v)>();
                    cand.Add((a, b, x));
                    if (a < op1) cand.Add((a + 1, b, (x + 1) / 2));
                    if (b < op2 && x >= k) cand.Add((a, b + 1, x - k));
                    if (a < op1 && b < op2) {
                        int v1 = (x + 1) / 2;
                        if (v1 >= k) cand.Add((a + 1, b + 1, v1 - k));
                        if (x >= k) cand.Add((a + 1, b + 1, (x - k + 1) / 2));
                    }
                    foreach (var c in cand) {
                        if (dp[a][b] + c.v < ndp[c.na][c.nb]) ndp[c.na][c.nb] = dp[a][b] + c.v;
                    }
                }
            }
            dp = ndp;
        }
        long ans = inf;
        for (int a = 0; a <= op1; a++)
            for (int b = 0; b <= op2; b++)
                if (dp[a][b] < ans) ans = dp[a][b];
        return (int)ans;
    }
}
