// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minOperations = function(nums, x) {
    const target = nums.reduce((a, b) => a + b, 0) - x;
    if (target < 0) return -1;
    let best = -1, left = 0, cur = 0;
    for (let right = 0; right < nums.length; right++) {
        cur += nums[right];
        while (cur > target) {
            cur -= nums[left++];
        }
        if (cur === target) best = Math.max(best, right - left + 1);
    }
    return best < 0 ? -1 : nums.length - best;
};
