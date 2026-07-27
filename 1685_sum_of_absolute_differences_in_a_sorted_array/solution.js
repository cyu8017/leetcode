// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSumAbsoluteDifferences = function(nums) {
    const total = nums.reduce((a, b) => a + b, 0);
    let left = 0;
    const n = nums.length;
    const ans = [];
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        ans.push(x * i - left + (total - left - x) - x * (n - i - 1));
        left += x;
    }
    return ans;
};
