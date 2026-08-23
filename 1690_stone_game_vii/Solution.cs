// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

using System;

public class Solution {
    public int StoneGameVII(int[] stones) {
        int n = stones.Length;
        int[] pre = new int[n + 1];
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + stones[i];
        int[,] dp = new int[n, n];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                dp[i, j] = Math.Max(
                    pre[j + 1] - pre[i + 1] - dp[i + 1, j],
                    pre[j] - pre[i] - dp[i, j - 1]);
            }
        }
        return dp[0, n - 1];
    }
}
