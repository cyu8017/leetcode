// LeetCode 1458 - Max Dot Product Of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

public class Solution {
    public int MaxDotProduct(int[] nums1, int[] nums2) {
        int n = nums2.Length;
        var dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = long.MinValue / 4;
        foreach (int a in nums1) {
            var prev = (long[])dp.Clone();
            for (int j = 1; j <= n; j++) {
                long product = (long)a * nums2[j - 1];
                dp[j] = System.Math.Max(dp[j - 1], System.Math.Max(prev[j],
                    System.Math.Max(product, product + System.Math.Max(0, prev[j - 1]))));
            }
        }
        return (int)dp[n];
    }
}
