// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

import java.util.Arrays;

class Solution {
    public long minimumCost(int[] nums, int[] cost, int k) {
        int n = nums.length;
        long[] pn = new long[n + 1], pc = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pn[i + 1] = pn[i] + nums[i];
            pc[i + 1] = pc[i] + cost[i];
        }
        final long inf = 1L << 62;
        long[] dp = new long[n + 1];
        Arrays.fill(dp, 0);
        for (int i = 0; i < n; i++) dp[i] = inf;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                long cand = pn[j + 1] * (pc[j + 1] - pc[i]) + (long) k * (pc[n] - pc[i]) + dp[j + 1];
                if (cand < dp[i]) dp[i] = cand;
            }
        }
        return dp[0];
    }
}
