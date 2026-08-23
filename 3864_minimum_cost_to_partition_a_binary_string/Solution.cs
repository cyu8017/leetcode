// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

using System;

public class Solution {
    public long MinCost(string s, int encCost, int flatCost) {
        int n = s.Length;
        var pre = new int[n + 1];
        for (int i = 1; i <= n; i++) pre[i] = pre[i - 1] + (s[i - 1] - '0');
        long Dfs(int l, int r) {
            int x = pre[r] - pre[l];
            long res = x != 0 ? (long)(r - l) * x * encCost : flatCost;
            if ((r - l) % 2 == 0) {
                int m = (l + r) / 2;
                res = Math.Min(res, Dfs(l, m) + Dfs(m, r));
            }
            return res;
        }
        return Dfs(0, n);
    }
}
