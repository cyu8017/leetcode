// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

class Solution {
    public int[] solve(int[] nums, int[][] queries) {
        final long mod = 1_000_000_007L;
        int n = nums.length;
        int block = (int) Math.sqrt(n) + 1;
        int[][] dp = new int[block][n];
        for (int step = 1; step < block; step++) {
            for (int i = n - 1; i >= 0; i--) {
                long next = i + step < n ? dp[step][i + step] : 0;
                dp[step][i] = (int) ((nums[i] + next) % mod);
            }
        }
        int[] ans = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int start = queries[q][0];
            int step = queries[q][1];
            if (step < block) {
                ans[q] = dp[step][start];
            } else {
                long total = 0;
                for (int i = start; i < n; i += step) {
                    total += nums[i];
                }
                ans[q] = (int) (total % mod);
            }
        }
        return ans;
    }
}
