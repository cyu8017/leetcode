// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

export function maxSubarraySumCircular(nums: number[]): number {
    let total = 0;
    for (const x of nums) total += x;
    let maxSum = nums[0], minSum = nums[0], curMax = nums[0], curMin = nums[0];
    for (let i = 1; i < nums.length; i++) {
        curMax = Math.max(nums[i], curMax + nums[i]);
        curMin = Math.min(nums[i], curMin + nums[i]);
        maxSum = Math.max(maxSum, curMax);
        minSum = Math.min(minSum, curMin);
    }
    if (maxSum < 0) return maxSum;
    return Math.max(maxSum, total - minSum);
}
