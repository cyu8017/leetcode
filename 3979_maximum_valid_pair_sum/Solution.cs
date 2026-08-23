// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

using System;

public class Solution {
    public int MaxValidPairSum(int[] nums, int k) {
        int ans = 0, x = 0;
        for (int j = k; j < nums.Length; j++) {
            int y = nums[j];
            x = Math.Max(x, nums[j - k]);
            ans = Math.Max(ans, x + y);
        }
        return ans;
    }
}
