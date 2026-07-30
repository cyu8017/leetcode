// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

using System;

public class Solution {
    public int StoneGameII(int[] piles) {
        int n = piles.Length;
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) suffix[i] = suffix[i + 1] + piles[i];
        int[,] memo = new int[n, n + 1];
        for (int i = 0; i < n; i++)
            for (int j = 0; j <= n; j++)
                memo[i, j] = -1;

        int Dfs(int i, int m) {
            if (i >= n) return 0;
            if (i + 2 * m >= n) return suffix[i];
            if (memo[i, m] != -1) return memo[i, m];
            int bestOpp = int.MaxValue;
            for (int x = 1; x <= Math.Min(2 * m, n - i); x++)
                bestOpp = Math.Min(bestOpp, Dfs(i + x, Math.Max(x, m)));
            return memo[i, m] = suffix[i] - bestOpp;
        }

        return Dfs(0, 1);
    }
}
