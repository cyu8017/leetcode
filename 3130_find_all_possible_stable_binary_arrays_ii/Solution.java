// LeetCode 3130 - Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

import java.util.Arrays;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int limit;
    private int[][][] f;

    private int dfs(int i, int j, int k) {
        if (i < 0 || j < 0) return 0;
        if (i == 0) return (k == 1 && j <= limit) ? 1 : 0;
        if (j == 0) return (k == 0 && i <= limit) ? 1 : 0;
        if (f[i][j][k] != -1) return f[i][j][k];
        int res;
        if (k == 0)
            res = (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD;
        else
            res = (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD;
        return f[i][j][k] = res;
    }

    public int numberOfStableArrays(int zero, int one, int limit) {
        this.limit = limit;
        f = new int[zero + 1][one + 1][2];
        for (int[][] a : f) for (int[] b : a) Arrays.fill(b, -1);
        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD;
    }
}
