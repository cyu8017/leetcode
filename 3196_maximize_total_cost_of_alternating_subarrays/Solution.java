// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

class Solution {
    private static final long NEG = (long) -1e18;
    private int[] nums;
    private long[][] memo;
    private int n;

    public long maximumTotalCost(int[] nums) {
        this.nums = nums;
        n = nums.length;
        memo = new long[n][2];
        for (int i = 0; i < n; i++) {
            memo[i][0] = memo[i][1] = NEG;
        }
        return dfs(0, 0);
    }

    private long dfs(int i, int j) {
        if (i >= n) {
            return 0;
        }
        if (memo[i][j] != NEG) {
            return memo[i][j];
        }
        long res = nums[i] + dfs(i + 1, 1);
        if (j > 0) {
            res = Math.max(res, -nums[i] + dfs(i + 1, 0));
        }
        return memo[i][j] = res;
    }
}
