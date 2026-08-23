// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

/**
 * @param {number[]} nums
 * @param {number} key
 * @return {number}
 */
var mostFrequent = function(nums, key) {
    const freq = new Map();
    let best = 0, ans = 0;
    for (let i = 0; i + 1 < nums.length; i++) {
        if (nums[i] === key) {
            const v = (freq.get(nums[i + 1]) || 0) + 1;
            freq.set(nums[i + 1], v);
            if (v > best) { best = v; ans = nums[i + 1]; }
        }
    }
    return ans;
};
