// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

class Solution {
    public int validSubarraySplit(int[] nums) {
        int n = nums.length;
        final int INF = 1 << 30;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] >= INF) continue;
            for (int j = i; j < n; j++) {
                if (gcd(nums[i], nums[j]) > 1) {
                    if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
                }
            }
        }
        return dp[n] >= INF ? -1 : dp[n];
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
