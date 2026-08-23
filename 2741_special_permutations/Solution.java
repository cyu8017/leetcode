// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

import java.util.Arrays;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int[] nums;
    private int[][] memo;

    public int specialPerm(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        memo = new int[1 << n][n];
        for (int[] row : memo) Arrays.fill(row, -1);
        int ans = 0;
        for (int i = 0; i < n; i++) ans = (ans + dfs(1 << i, i)) % MOD;
        return ans;
    }

    private int dfs(int mask, int last) {
        if (mask == (1 << nums.length) - 1) return 1;
        if (memo[mask][last] != -1) return memo[mask][last];
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((mask & (1 << i)) != 0) continue;
            if (nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0)
                res = (res + dfs(mask | (1 << i), i)) % MOD;
        }
        return memo[mask][last] = res;
    }
}
