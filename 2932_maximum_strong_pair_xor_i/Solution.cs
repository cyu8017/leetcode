// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

using System;

public class Solution {
    public int MaximumStrongPairXor(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.Length; i++)
            for (int j = i; j < nums.Length; j++) {
                int x = nums[i], y = nums[j];
                if (Math.Abs(x - y) <= Math.Min(x, y)) {
                    int xorr = x ^ y;
                    if (xorr > ans) ans = xorr;
                }
            }
        return ans;
    }
}
