// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

using System;

public class Solution {
    public int MaximumStrongPairXor(int[] nums) {
        Array.Sort(nums);
        int ans = 0;
        for (int i = 0; i < nums.Length; i++) {
            int x = nums[i];
            for (int j = i; j < nums.Length && nums[j] <= 2 * x; j++) {
                int xorr = x ^ nums[j];
                if (xorr > ans) ans = xorr;
            }
        }
        return ans;
    }
}
