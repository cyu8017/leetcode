// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

public class Solution {
    public long MinArraySum(int[] nums, int k) {
        int n = nums.Length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = (prefix[i] + nums[i]) % k;
        const long inf = 1L << 62;
        long[] dp = new long[n + 1], best = new long[k];
        for (int i = 0; i < k; i++) best[i] = inf;
        best[0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + nums[i - 1];
            if (best[prefix[i]] < dp[i]) dp[i] = best[prefix[i]];
            if (dp[i] < best[prefix[i]]) best[prefix[i]] = dp[i];
        }
        return dp[n];
    }
}
