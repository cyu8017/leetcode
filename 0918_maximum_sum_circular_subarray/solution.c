// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

int maxSubarraySumCircular(int* nums, int numsSize) {
    int total = nums[0];
    int maxSum = nums[0], minSum = nums[0];
    int curMax = nums[0], curMin = nums[0];
    for (int i = 1; i < numsSize; i++) {
        int x = nums[i];
        total += x;
        curMax = x > curMax + x ? x : curMax + x;
        curMin = x < curMin + x ? x : curMin + x;
        if (curMax > maxSum) maxSum = curMax;
        if (curMin < minSum) minSum = curMin;
    }
    if (maxSum < 0) return maxSum;
    int circ = total - minSum;
    return maxSum > circ ? maxSum : circ;
}
