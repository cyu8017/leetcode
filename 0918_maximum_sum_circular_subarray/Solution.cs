// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

using System;
using System.Linq;

public class Solution {
    public int MaxSubarraySumCircular(int[] nums) {
        int total = nums.Sum();
        int maxSum = nums[0], minSum = nums[0], curMax = nums[0], curMin = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            curMax = Math.Max(nums[i], curMax + nums[i]);
            curMin = Math.Min(nums[i], curMin + nums[i]);
            maxSum = Math.Max(maxSum, curMax);
            minSum = Math.Min(minSum, curMin);
        }
        if (maxSum < 0) return maxSum;
        return Math.Max(maxSum, total - minSum);
    }
}
