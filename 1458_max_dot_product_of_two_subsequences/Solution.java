// LeetCode 1458 - Max Dot Product Of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int n = nums2.length;
        var dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = Long.MIN_VALUE / 4;
        for (int a : nums1) {
            var prev = (long[])dp.Clone();
            for (int j = 1; j <= n; j++) {
                long product = (long)a * nums2[j - 1];
                dp[j] = Math.max(dp[j - 1], Math.max(prev[j],
                    Math.max(product, product + Math.max(0, prev[j - 1]))));
            }
        }
        return (int)dp[n];
    }
}
