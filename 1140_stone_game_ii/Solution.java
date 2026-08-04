// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) suffix[i] = suffix[i + 1] + piles[i];
        int[][] memo = new int[n][n + 1];
        for (int[] row : memo) java.util.Arrays.fill(row, -1);
        return dfs(0, 1, piles, suffix, memo);
    }

    private int dfs(int i, int m, int[] piles, int[] suffix, int[][] memo) {
        int n = piles.length;
        if (i >= n) return 0;
        if (i + m >= n) return suffix[i];
        if (memo[i][m] != -1) return memo[i][m];
        int bestOpp = Integer.MAX_VALUE;
        for (int x = 1; x <= Math.min(2 * m, n - i); x++) {
            bestOpp = Math.min(bestOpp, dfs(i + x, Math.max(x, m), piles, suffix, memo));
        }
        return memo[i][m] = suffix[i] - bestOpp;
    }
}
