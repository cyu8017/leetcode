// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

/**
 * @param {number[]} nums
 * @return {number}
 */
var blockCount = function(nums) {
    if (!nums.length) return 0;
    let ans = 1;
    for (let i = 1; i < nums.length; i++)
        if (nums[i] !== nums[i - 1]) ans++;
    return ans;
};
