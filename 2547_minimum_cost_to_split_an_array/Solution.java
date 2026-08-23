// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minCost(int[] nums, int k) {
        int n = nums.length;
        final long INF = 1_000_000_000_000_000_000L;
        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) dp[i] = INF;
        for (int i = 0; i < n; ++i) {
            Map<Integer, Integer> freq = new HashMap<>();
            int trimmed = 0;
            for (int j = i; j < n; ++j) {
                int c = freq.getOrDefault(nums[j], 0) + 1;
                freq.put(nums[j], c);
                if (c == 2) trimmed += 2;
                else if (c > 2) trimmed++;
                long cost = dp[i] + k + trimmed;
                if (cost < dp[j + 1]) dp[j + 1] = cost;
            }
        }
        return (int) dp[n];
    }
}
