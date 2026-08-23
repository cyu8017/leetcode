// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

using System;

public class Solution {
    public long MaximumScore(int[] nums) {
        int n = nums.Length;
        long[] suf = new long[n];
        suf[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) suf[i] = Math.Min(nums[i], suf[i + 1]);
        long pre = 0;
        long ans = long.MinValue;
        for (int i = 0; i < n - 1; i++) {
            pre += nums[i];
            ans = Math.Max(ans, pre - suf[i + 1]);
        }
        return ans;
    }
}
