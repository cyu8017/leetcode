// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

using System;

public class Solution {
    public long MaxAlternatingSum(int[] nums) {
        for (int i = 0; i < nums.Length; i++) nums[i] *= nums[i];
        Array.Sort(nums);
        int m = nums.Length / 2;
        long ans = 0;
        for (int i = 0; i < m; i++) ans -= nums[i];
        for (int i = m; i < nums.Length; i++) ans += nums[i];
        return ans;
    }
}
