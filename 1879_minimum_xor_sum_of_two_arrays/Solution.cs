// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

public class Solution {
    public int MinimumXORSum(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        var dp = new int[1 << n];
        Array.Fill(dp, int.MaxValue / 2);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int i = BitCount(mask);
            if (i >= n) {
                continue;
            }
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << j)) == 0) {
                    int nextMask = mask | (1 << j);
                    int cost = dp[mask] + (nums1[i] ^ nums2[j]);
                    if (cost < dp[nextMask]) {
                        dp[nextMask] = cost;
                    }
                }
            }
        }
        return dp[(1 << n) - 1];
    }

    private static int BitCount(int value) {
        int count = 0;
        while (value != 0) {
            count += value & 1;
            value >>= 1;
        }
        return count;
    }
}
