// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    nums = nums.slice().sort((a, b) => a - b);
    let best = 0;
    for (let i = 0; i < nums.length / 2; i++) {
        best = Math.max(best, nums[i] + nums[nums.length - 1 - i]);
    }
    return best;
};
