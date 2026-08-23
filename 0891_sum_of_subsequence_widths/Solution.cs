// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

using System;

public class Solution {
    public int SumSubseqWidths(int[] nums) {
        const int MOD = 1000000007;
        Array.Sort(nums);
        int n = nums.Length;
        long[] pow2 = new long[n];
        pow2[0] = 1;
        for (int i = 1; i < n; i++) pow2[i] = (pow2[i - 1] * 2) % MOD;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans + nums[i] * (pow2[i] - pow2[n - 1 - i])) % MOD;
        }
        return (int)((ans + MOD) % MOD);
    }
}
