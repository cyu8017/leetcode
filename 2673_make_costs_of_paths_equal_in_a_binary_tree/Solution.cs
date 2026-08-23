// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

using System;

public class Solution {
    public int MinIncrements(int n, int[] cost) {
        int ans = 0;
        for (int i = n / 2 - 1; i >= 0; i--) {
            int l = 2 * i + 1, r = 2 * i + 2;
            ans += Math.Abs(cost[l] - cost[r]);
            cost[i] += Math.Max(cost[l], cost[r]);
        }
        return ans;
    }
}
