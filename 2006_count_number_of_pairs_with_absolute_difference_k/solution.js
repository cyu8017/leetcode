// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countKDifference = function(nums, k) {
    const freq = new Map();
    let ans = 0;
    for (const x of nums) {
        ans += freq.get(x - k) || 0;
        ans += freq.get(x + k) || 0;
        freq.set(x, (freq.get(x) || 0) + 1);
    }
    return ans;
};
