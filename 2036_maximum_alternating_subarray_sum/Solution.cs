// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

using System;

public class Solution {
    public long MaximumAlternatingSubarraySum(int[] nums) {
        long ans = long.MinValue, even = 0, odd = 0;
        for (int i = 0; i < nums.Length; i++) {
            long x = nums[i];
            if (i % 2 == 0) even += x;
            else even = Math.Max(0L, even - x);
            ans = Math.Max(ans, even);
        }
        even = 0;
        for (int i = 1; i < nums.Length; i++) {
            long x = nums[i];
            if (i % 2 == 1) odd += x;
            else odd = Math.Max(0L, odd - x);
            ans = Math.Max(ans, odd);
        }
        return ans;
    }
}
