// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        int maxSum = nums[0], minSum = nums[0], curMax = nums[0], curMin = nums[0];
        for (int i = 1; i < nums.length; i++) {
            curMax = Math.max(nums[i], curMax + nums[i]);
            curMin = Math.min(nums[i], curMin + nums[i]);
            maxSum = Math.max(maxSum, curMax);
            minSum = Math.min(minSum, curMin);
        }
        if (maxSum < 0) return maxSum;
        return Math.max(maxSum, total - minSum);
    }
}
