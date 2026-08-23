// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

import java.util.Arrays;

class Solution {
    public int minimumXORSum(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int size = 1 << n;
        int[] dp = new int[size];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int mask = 0; mask < size; mask++) {
            int i = Integer.bitCount(mask);
            if (i >= n) {
                continue;
            }
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << j)) != 0) {
                    continue;
                }
                int nextMask = mask | (1 << j);
                int cost = dp[mask] + (nums1[i] ^ nums2[j]);
                if (cost < dp[nextMask]) {
                    dp[nextMask] = cost;
                }
            }
        }

        return dp[size - 1];
    }
}
