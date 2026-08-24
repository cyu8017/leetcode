// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToSplitArray = function(nums) {
    let total = 0;
    for (const v of nums) total += v;
    let left = 0, ans = 0;
    for (let i = 0; i + 1 < nums.length; i++) {
        left += nums[i];
        if (left >= total - left) ans++;
    }
    return ans;
};
