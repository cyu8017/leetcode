// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countBadPairs = function(nums) {
    const n = nums.length;
    const total = n * (n - 1) / 2;
    const freq = new Map();
    let good = 0;
    for (let i = 0; i < nums.length; i++) {
        const key = nums[i] - i;
        good += freq.get(key) || 0;
        freq.set(key, (freq.get(key) || 0) + 1);
    }
    return total - good;
};
