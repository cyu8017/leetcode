// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

class Solution {
    private int[] nums;
    private long[][] f;
    private int n;

    public long minIncrease(int[] nums) {
        this.nums = nums;
        n = nums.length;
        f = new long[n][2];
        for (int i = 0; i < n; i++) f[i][0] = f[i][1] = -1;
        return dfs(1, (n & 1) ^ 1);
    }

    private long dfs(int i, int j) {
        if (i >= n - 1) return 0;
        if (f[i][j] != -1) return f[i][j];
        int cost = Math.max(0, Math.max(nums[i - 1], nums[i + 1]) + 1 - nums[i]);
        long ans = (long) cost + dfs(i + 2, j);
        if (j > 0) ans = Math.min(ans, dfs(i + 1, 0));
        return f[i][j] = ans;
    }
}
